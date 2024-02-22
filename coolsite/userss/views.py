from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from rest_framework.reverse import reverse_lazy

from product.utils import DataMixin
from userss.forms import LoginForm, RegisterForm, UpdateProfileForm


class UserProfile(DataMixin, UpdateView):
    form_class = UpdateProfileForm
    model = get_user_model()
    template_name = 'userss/user_profile.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfile, self).get_context_data()
        c_def = self.get_user_context(title='Ваш профиль')
        return dict(list(context.items())+list(c_def.items()))


class Register(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'userss/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Register, self).get_context_data()
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'userss/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Login, self).get_context_data()
        c_def = self.get_user_context(title='Вход в аккаунт')
        return dict(list(context.items())+list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('home')
