# Generated by Django 4.0.5 on 2022-07-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_vendors_vend_email_alter_vendors_vend_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMaster',
            fields=[
                ('ad_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ad_name', models.CharField(max_length=100)),
                ('ad_mobile', models.CharField(max_length=100)),
                ('ad_email', models.CharField(max_length=100)),
                ('ad_password', models.CharField(max_length=100)),
                ('ad_role', models.CharField(max_length=100)),
                ('ad_status', models.CharField(max_length=100)),
                ('ad_created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('ct_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ct_name', models.CharField(max_length=100)),
                ('ct_image', models.CharField(max_length=100)),
                ('ct_weight', models.CharField(max_length=100)),
                ('ct_price', models.CharField(max_length=100)),
                ('ct_total_amount', models.IntegerField()),
                ('ct_ordered_by', models.CharField(max_length=100)),
                ('ct_status', models.CharField(max_length=100)),
                ('ct_created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('or_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('or_name', models.CharField(max_length=100)),
                ('or_weight', models.CharField(max_length=100)),
                ('or_rate', models.CharField(max_length=100)),
                ('or_total_amount', models.CharField(max_length=100)),
                ('or_address', models.CharField(max_length=100)),
                ('or_ordered_by', models.CharField(max_length=100)),
                ('or_date', models.CharField(max_length=100)),
                ('or_transaction_id', models.CharField(max_length=100)),
                ('or_status', models.CharField(max_length=100)),
                ('or_created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('rg_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('rg_name', models.CharField(max_length=100)),
                ('rg_mobile', models.CharField(max_length=100)),
                ('rg_email', models.CharField(max_length=100)),
                ('rg_password', models.CharField(max_length=100)),
                ('rg_address', models.CharField(max_length=100)),
                ('rg_status', models.CharField(max_length=100)),
            ],
        ),
    ]
