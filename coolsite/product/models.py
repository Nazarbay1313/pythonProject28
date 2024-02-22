from django.db import models
from django.urls import reverse

from coolsite.settings import AUTH_USER_MODEL

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=156, verbose_name='Наименование')
    slug = models.SlugField(unique=True, db_index=True, null=True, verbose_name='Слаг')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(default=0, null=True)
    content = models.TextField(verbose_name='Описание')
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products', verbose_name='Фото', null=True, blank=True)
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукты'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=156, verbose_name='Наименование тега')
    slug = models.SlugField(db_index=True, unique=True)

    class Meta:
        verbose_name = 'Ингридиенты'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag_slug': self.slug})


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'

    def __str__(self):
        return f"Корзина {self.product}"

    def sum(self):
        return self.product.price * self.quantity


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_query_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарии'
        ordering = ('-id',)

    def __str__(self):
        return f"Комментарий пользователя {self.user}"


class ProductShots(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_shots', null=True)

    class Meta:
        verbose_name = 'Фото'
        ordering = ('-id',)

    def __str__(self):
        return f"Картинка для {self.product}"


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
