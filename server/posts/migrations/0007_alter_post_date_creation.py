# Generated by Django 5.0.7 on 2024-07-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_creation',
            field=models.DateField(verbose_name='Дата создания'),
        ),
    ]
