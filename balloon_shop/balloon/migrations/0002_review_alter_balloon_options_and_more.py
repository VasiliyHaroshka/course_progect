# Generated by Django 4.1.2 on 2022-10-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balloon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='отзыв')),
                ('text', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/reviews_photo', verbose_name='адрес фото')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='balloon',
            options={'ordering': ['-time_modified'], 'verbose_name': 'Шар', 'verbose_name_plural': 'Шары'},
        ),
        migrations.AlterField(
            model_name='balloon',
            name='time_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='время изменения'),
        ),
    ]