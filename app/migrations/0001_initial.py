# Generated by Django 4.0.4 on 2022-06-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cat_image', models.ImageField(upload_to='app/static/media/products/')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_status', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ap_image', models.ImageField(upload_to='app/static/media/products/')),
                ('ap_type', models.CharField(max_length=100)),
                ('ap_name', models.CharField(max_length=100)),
                ('ap_weight', models.CharField(max_length=100)),
                ('ap_rate', models.CharField(max_length=100)),
                ('ap_description', models.CharField(max_length=100)),
                ('ap_status', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('vend_id', models.AutoField(default='', primary_key=True, serialize=False, unique=True)),
                ('vend_shopname', models.CharField(default='', max_length=80)),
                ('vend_name', models.CharField(max_length=80)),
                ('vend_contact', models.CharField(max_length=80)),
                ('vend_email', models.CharField(default='', max_length=80)),
                ('vend_place', models.CharField(max_length=80)),
                ('vend_status', models.CharField(default='0', max_length=80)),
            ],
        ),
    ]
