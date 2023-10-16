from django.db import models
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    date_of_change = models.DateTimeField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.price} рублей'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


class Post(models.Model):
    name = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published = models.BooleanField(verbose_name='признак публикации', default=True)
    views_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.slug is None:
            self.slug = slugify(self.name)

    def __str__(self):
        return f'{self.name} {self.slug}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def increase_views_count(self):
        """
        Увеличивает просмотры поста на 1.
        """
        self.views_count += 1
        self.save()


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.IntegerField(verbose_name='номер версии')
    title_version = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='признак текущей версии', default=True)

    def __str__(self):
        return f'{self.title_version} ({self.product})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
