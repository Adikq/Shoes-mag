from django.db import models
from django.urls import reverse


class ShoesCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='Url')

    class Meta:
        verbose_name = 'Категория обуви'
        verbose_name_plural = 'Категории обуви'

    def __str__(self):
            return f'{self.id}. {self.title}'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class ShoesSize(models.Model):
    size = models.SmallIntegerField(default=0, verbose_name='Размер обуви')

    class Meta:
        verbose_name = 'Размер обуви'
        verbose_name_plural = 'Размеры обуви'

    def __str__(self):
        return f'Размер: {self.size}'

class Shoes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название обуви')
    img = models.ImageField(upload_to='shoes/%Y/%m/%d', verbose_name='Фото')
    price = models.SmallIntegerField(default=0, verbose_name='Цена')
    color = models.CharField(max_length=255, verbose_name='Цвет обуви')
    size = models.ManyToManyField(ShoesSize, verbose_name='Размер')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='Url')
    category = models.ForeignKey(ShoesCategory, on_delete=models.PROTECT, verbose_name='Категория обуви')

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обуви'

    def __str__(self):
        return f'{self.id}. {self.title}'

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'slug': self.slug})

class ShoesPhoto(models.Model):
    img = models.ImageField(upload_to='shoes_photo/%Y/%m/%d', verbose_name='Дополнительные фото')
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, verbose_name='Обувь')

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'



class Order(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.PROTECT,verbose_name='Обувь')
    name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    number = models.CharField(max_length=255, verbose_name='Номер')
    address= models.CharField(max_length=255, verbose_name='Адресс')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'