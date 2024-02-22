from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from product.forms import CommentForm, ContactForm
from product.models import Basket, Comment, Contact, Product
from product.tasks import send_spam_email
from product.utils import DataMixin

# Create your views here.


class HomeView(DataMixin, ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data()
        c_def = self.get_user_context(title='STORE - Каталог')
        return dict(list(context.items())+list(c_def.items()))


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)

    basket.quantity -= 1
    basket.save()

    if basket.quantity == 0:
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class ProductDetail(DataMixin, DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items())+list(c_def.items()))


class Tags(DataMixin, ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs['tag_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Tags, self).get_context_data()
        c_def = self.get_user_context(title='STORE - Каталог')
        return dict(list(context.items())+list(c_def.items()))


class Order(DataMixin, ListView):
    model = Basket
    context_object_name = 'baskets'
    template_name = 'product/order.html'

    def get_queryset(self):
        return Basket.objects.all().select_related('user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Order, self).get_context_data()
        c_def = self.get_user_context(title='Только для администратора')
        return dict(list(context.items())+list(c_def.items()))


class AboutUs(DataMixin, TemplateView):
    template_name = 'product/about_us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AboutUs, self).get_context_data()
        c_def = self.get_user_context(title='Информация о нас')
        return dict(list(context.items())+list(c_def.items()))


class Success(DataMixin, TemplateView):
    template_name = 'product/success.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Success, self).get_context_data()
        c_def = self.get_user_context(title='Поздравляем')
        return dict(list(context.items())+list(c_def.items()))


class Baskets(DataMixin, ListView):
    model = Basket
    template_name = 'product/basket.html'
    context_object_name = 'baskets'

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Baskets, self).get_context_data()
        c_def = self.get_user_context(title='Корзина')
        return dict(list(context.items())+list(c_def.items()))


def comment_add(request, product_id):
    product = Product.objects.get(id=product_id)
    comment = Comment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect(comment_add, product_id)
    else:
        form = CommentForm()

    return render(request, 'product/comments.html', {
        'product': product,
        'comment': comment,
        'form': form,
    })


class ContactView(DataMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'product/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactView, self).get_context_data()
        c_def = self.get_user_context(title='Оповестите пользователя о наших новинках!')
        return dict(list(context.items())+list(c_def.items()))
