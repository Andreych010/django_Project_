# Generated by Django 4.2.3 on 2023-07-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_post/', verbose_name='изображение')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('sign_publication', models.BooleanField(verbose_name='признак публикации')),
                ('number_views', models.IntegerField(verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'наименование',
                'verbose_name_plural': 'Blog',
                'ordering': ('id',),
            },
        ),
    ]
