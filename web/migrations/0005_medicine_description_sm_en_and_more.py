# Generated by Django 5.0 on 2024-11-11 15:54

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_medicine_description_remove_medicine_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='description_sm_en',
            field=django_ckeditor_5.fields.CKEditor5Field(default='', verbose_name='Tavsif kichik [en]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='description_sm_ru',
            field=django_ckeditor_5.fields.CKEditor5Field(default='', verbose_name='Tavsif kichik [ru]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='description_sm_uz',
            field=django_ckeditor_5.fields.CKEditor5Field(default='', verbose_name='Tavsif kichik [uz]'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description_en',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Tavsif [en]'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description_ru',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Tavsif [ru]'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description_uz',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Tavsif [uz]'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Nomi [en]'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name_ru',
            field=models.CharField(max_length=200, verbose_name='Nomi [ru]'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name_uz',
            field=models.CharField(max_length=200, verbose_name='Nomi [uz]'),
        ),
    ]