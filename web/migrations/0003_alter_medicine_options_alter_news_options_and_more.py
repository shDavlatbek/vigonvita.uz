# Generated by Django 5.0 on 2024-11-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_news_views_alter_medicine_image_alter_news_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Dorilar', 'verbose_name_plural': 'Dorilar'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Yangiliklar', 'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='', verbose_name='Qisqa link'),
        ),
    ]