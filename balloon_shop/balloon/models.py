from django.db import models
from django.urls import reverse


class Balloon(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    photo = models.ImageField(upload_to='photos/', verbose_name='адрес фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_modified = models.DateTimeField(auto_now=True, verbose_name='время изменения')
    is_onsite = models.BooleanField(default=True, verbose_name='публикация')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='группа')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'good_slug': self.slug}) # маршрут к конкретной записи

    class Meta:
        verbose_name = "Шар"
        verbose_name_plural = "Шары"
        ordering = ['-time_modified']


class Group(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_slug': self.slug}) # маршрут к конкретной группе

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['id']


class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name="отзыв")
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/reviews_photo', blank=True, verbose_name='адрес фото')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_on']