# Generated by Django 4.0.5 on 2022-07-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_vendors_vend_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ap_created_by',
            field=models.CharField(default='', max_length=100),
        ),
    ]
