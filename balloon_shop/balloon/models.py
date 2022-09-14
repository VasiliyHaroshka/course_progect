from django.db import models
from django.urls import reverse


class Balloon(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    photo = models.ImageField(upload_to='photos/', verbose_name='адрес фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_modified = models.DateTimeField(auto_now=True, verbose_name='вермя изменения')
    is_onsite = models.BooleanField(default=True, verbose_name='публикация')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, verbose_name='группа')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'good_id': self.pk}) # маршрут к конкретной записи

    class Meta:
        verbose_name = "Шар"
        verbose_name_plural = "Шары"
        ordering = ['time_modified']


class Group(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='название')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_id': self.pk}) # маршрут к конкретной записи

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['id']