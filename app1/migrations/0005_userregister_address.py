# Generated by Django 4.2.4 on 2023-08-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_type_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
