# Generated by Django 4.2.4 on 2023-08-18 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True, auto_now=True)),
                ('userid', models.CharField(max_length=250)),
                ('productid', models.CharField(max_length=250)),
                ('quantity', models.CharField(max_length=250)),
                ('paymentamt', models.CharField(max_length=250)),
                ('paymentmethod', models.CharField(max_length=250)),
                ('transactionid', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Userregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='product_Img')),
                ('quantity', models.IntegerField()),
                ('categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
