from django.db import models
from msilib import add_tables

# Create your models here.
class AdminMaster(models.Model):
	ad_id = models.AutoField(primary_key=True, unique = True)
	ad_name = models.CharField(max_length=100)
	ad_mobile = models.CharField(max_length=100)
	ad_email = models.CharField(max_length=100)
	ad_password = models.CharField(max_length=100)
	ad_role = models.CharField(max_length=100)
	ad_status = models.CharField(max_length=100)
	ad_created_by = models.CharField(max_length=100)

class Product(models.Model):
	ap_id = models.AutoField(primary_key=True, unique = True)
	ap_image = models.ImageField(upload_to="app/static/media/products/")
	ap_type = models.CharField(max_length=100)
	ap_name = models.CharField(max_length=100)
	ap_weight = models.CharField(max_length=100)
	ap_rate = models.CharField(max_length=100)
	ap_description = models.CharField(max_length=100)
	ap_status = models.CharField(max_length=100, default=0)
	ap_created_by = models.CharField(max_length=100, default="")



# category modal
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True, unique = True)
    cat_image = models.ImageField(upload_to="app/static/media/products/")
    cat_name=models.CharField(max_length=50)
    cat_status=models.CharField(max_length=50, default="0")

# vendors details in admin

class Vendors(models.Model):
	vend_id = models.AutoField(primary_key=True, unique = True)
	vend_shopname = models.CharField(max_length=80, default="")
	vend_name = models.CharField(max_length=80)
	vend_contact = models.CharField(max_length=80)
	vend_email = models.CharField(max_length=80)
	vend_password = models.CharField(max_length=100, default="")
	vend_place = models.CharField(max_length=80)
	vend_status = models.CharField(max_length=80, default="0")

class Order(models.Model):
	or_id = models.AutoField(primary_key=True, unique = True)
	or_name = models.CharField(max_length=100)
	or_weight = models.CharField(max_length=100)
	or_rate = models.CharField(max_length=100)
	or_total_amount = models.CharField(max_length=100)
	or_address = models.CharField(max_length=100)
	or_ordered_by = models.CharField(max_length=100)
	or_date = models.CharField(max_length=100)
	or_transaction_id = models.CharField(max_length=100)
	or_status = models.CharField(max_length=100)
	or_created_by = models.CharField(max_length=100)

class Cart(models.Model):
	ct_id = models.AutoField(primary_key=True, unique = True)
	ct_name = models.CharField(max_length=100)
	ct_image = models.CharField(max_length=100)
	ct_weight = models.CharField(max_length=100)
	ct_price = models.CharField(max_length=100)
	ct_total_amount = models.IntegerField()
	ct_ordered_by = models.CharField(max_length=100)
	ct_status = models.CharField(max_length=100)
	ct_created_by = models.CharField(max_length=100)

class Register(models.Model):
	rg_id = models.AutoField(primary_key=True, unique = True)
	rg_name = models.CharField(max_length=100)
	rg_mobile = models.CharField(max_length=100)
	rg_email = models.CharField(max_length=100)
	rg_password = models.CharField(max_length=100)
	rg_address = models.CharField(max_length=100, default="")
	rg_status = models.CharField(max_length=100, default=0)

class PurchasedProducts(models.Model):
	ps_id = models.AutoField(primary_key=True, unique = True)
	ps_or_id = models.CharField(max_length=100)
	ps_product_name = models.CharField(max_length=100)
	ps_image = models.CharField(max_length=100)
	ps_weight = models.CharField(max_length=100)
	ps_price = models.CharField(max_length=100)
	ps_total_amt = models.CharField(max_length=100)
	ps_date = models.CharField(max_length=100)
	ps_status = models.CharField(max_length=100)
	ps_user_name = models.CharField(max_length=100)
	ps_user_email = models.CharField(max_length=100)
	ps_vendor_email = models.CharField(max_length=100)