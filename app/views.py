from django.shortcuts import render, HttpResponse
from app.models import Product
from app.models import Category
from app.models import Vendors
from django.http import  JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from app.models import AdminMaster
from app.models import Register
from app.models import Cart
from app.models import Order
from app.models import PurchasedProducts

import datetime;

# Create your views here.

def openweb(request):
    return render(request,'web/index.html')
# wlecome page
def openwelcome(request):
    return render(request,'web/welcome.html')

def aboutus(request):
    return render(request,'web/Aboutus.html')

def contact(request):
    return render(request,'web/contact.html')

def Gold(request):
    return render(request,'web/Gold.html')

def payment(request):
    return render(request,'web/payment.html')

def purity(request):
    return render(request,'web/purity.html')

def register(request):
    return render(request,'web/register.html')

def login(request):
    return render(request,'web/login.html')

def billing(request):
    return render(request,'web/Billling.html')

def shoping(request):
    return render(request,'web/shoping.html')

def cart(request):
    return render(request,'web/cart.html')

def check(request):
    return render(request,'web/check_out.html')

# admin pages funtions

def signin(request):
    return render(request,'admin/admin/signin.html')

def regadmin(request):
    return render(request,'admin/admin/registration.html')

def index1(request):
    return render(request,'admin/admin/index1.html')

def tables(request):
    return render(request,'admin/admin/tables.html')

def productad(request):
    return render(request,'admin/admin/product.html')

def cateadd(request):
    return render(request,'admin/admin/category.html')

def orderadd(request):
    return render(request,'admin/admin/order.html')

def vendoradd(request):
    return render(request,'admin/admin/vendors.html')

# vendor pages funtion

def vendorin(request):
    return render(request,'vendor/vendor/signin.html')

def vendorreg(request):
    return render(request,'vendor/vendor/register.html')

def vendorindex(request):
    return render(request,'vendor/vendor/index1.html')

def vendortab(request):
    return render(request,'vendor/vendor/tables.html')

def productad1(request):
    return render(request,'vendor/vendor/product.html')

def cateadd1(request):
    return render(request,'vendor/vendor/category.html')

def orderadd1(request):
    return render(request,'vendor/vendor/order.html')

def product_details(request):
    return render(request, 'web/product_details1.html')



# product add vendor

# def getProductData(request):
# 	# print(request.session['role']);

def ProductData(request):
    if request.POST['action'] == "getData":
        getData = Product.objects.filter(ap_status="0").values()
        data = list(getData)
        value = JsonResponse(data, safe=False);
        return value;

    elif request.POST['action'] == "add":
	    Product.objects.create(
		ap_image = request.FILES["filePhoto"],
		ap_type = request.POST["selType"],
		ap_name = request.POST['txtName'],
		ap_weight = request.POST['txtWeight'],
		ap_rate = request.POST['txtRate'],
        ap_description = request.POST['txtDesc'],
		ap_created_by = request.session['email']
    );

    elif request.POST['action'] == "update":
        Product.objects.filter(ap_id=request.POST['id']).update(
		ap_type = request.POST["selType1"],
		ap_name = request.POST['txtName1'],
		ap_weight = request.POST['txtWeight1'],
		ap_rate = request.POST['txtRate1'],
		ap_description = request.POST['txtDesc1']
    );
    
    elif request.POST['action'] == "delete":
        Product.objects.filter(ap_id=request.POST['id']).update(ap_status='1')
    return HttpResponse();
    
  

# juwels category 
def categoryDetails(request):
    if request.POST['action'] == "getData":
        getData = Category.objects.filter(cat_status="0").values()
        data = list(getData)
        value = JsonResponse(data, safe=False);
        return value;

    elif request.POST['action'] == "add":
        Category.objects.create(
        cat_image = request.FILES["filePhoto"],
        cat_name=request.POST['txtName1']);
    

    elif request.POST['action'] == "update":
	    Category.objects.filter(
        cat_id = request.POST['id']).update(
        cat_name = request.POST['txtName2'] );
        
    elif request.POST['action'] == "delete":
        Category.objects.filter(cat_id=request.POST['id']).update(cat_status='1')
    return HttpResponse();





# vendor adding funtion
def vendordetail(request):
    if request.POST['action'] == "getData":
        getData = Vendors.objects.filter(vend_status="0").values()
        data = list(getData)
        value = JsonResponse(data, safe=False);
        return value;
    
    elif request.POST['action'] == "add":
        Vendors.objects.create(
            vend_shopname = request.POST["txtName"],
            vend_name = request.POST['txtvenName'],
            vend_contact = request.POST["txtcontact"],
            vend_email = request.POST['txtemail'],
            vend_password = request.POST['txtPassword'],
            vend_place = request.POST["selType"] 
        
        );
    
    elif request.POST['action'] == "update":
	    Vendors.objects.filter(vend_id = request.POST['id']).update(
        vend_shopname = request.POST["txtName1"],
        vend_name = request.POST['txtvenName1'],
        vend_contact = request.POST["txtcontact1"],
        vend_email = request.POST['txtemail1'],
        vend_place = request.POST["selType1"] 
        
        );
    
    elif request.POST['action'] == "delete":
        Vendors.objects.filter(vend_id=request.POST['id']).update(vend_status='1')
    return HttpResponse();

def loginAdminDetails(request):

    if request.POST['action'] == "Admin":
        if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_password=request.POST['txtPassword'], ad_status=0).exists():
            data = AdminMaster.objects.filter(ad_email=request.POST['txtEmail']).values()
            data = list(data)
            dictValue = data[0]
            request.session['email'] = dictValue['ad_email']
            request.session['role'] = dictValue['ad_role']
            request.session['name'] = dictValue['ad_name']
            return HttpResponse(dictValue['ad_role'])
        else:
            return HttpResponse("0")

    else:
        if Vendors.objects.filter(vend_email=request.POST['txtEmail'], vend_password=request.POST['txtPassword'], vend_status=0).exists():
            data = Vendors.objects.filter(vend_email=request.POST['txtEmail']).values()
            data = list(data)
            dictValue = data[0]
            request.session['email'] = dictValue['vend_email']
            request.session['role'] = 'Vendor'
            request.session['name'] = dictValue['vend_name']
            return HttpResponse("Vendor")
        else:
            return HttpResponse("0")


def checkWebLogin(request):
    if Register.objects.filter(rg_email=request.POST['txtEmail'], rg_password=request.POST['txtPassword']).exists():
        request.session['web_email'] = request.POST['txtEmail']
        return HttpResponse("1")
    else:
        return HttpResponse("10")

def newRegister(request):

    if Register.objects.filter(rg_email=request.POST['txtEmail'], rg_mobile=request.POST['txtMobileNo']).exists():
        return HttpResponse('10')
    else:
        lclID = Register.objects.count()
        status = "0"
        lclNewID = lclID + 1

        Register.objects.create (
            rg_id = lclNewID,
            rg_name = request.POST['txtName'],
            rg_mobile = request.POST['txtMobileNo'],
            rg_email = request.POST['txtEmail'],
            rg_password = request.POST['txtPassword']

        )

        return HttpResponse('0')

def getWebProducts(request):

    getData = Product.objects.filter(ap_status="0").values();
    data = list(getData);
    value = JsonResponse(data, safe=False);
    return value;

def getSingleItem(request):
    products_json = Product.objects.filter(ap_id=request.POST['txtID']).values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def checkCheckout(request):
    if 'web_email' in request.session:
        return HttpResponse()
    else:
        return HttpResponse(0)

def addCart(request):

    if 'web_email' in request.session:
        products_json = Product.objects.filter(ap_id=request.POST['txtID']).values()
        data = list(products_json)
        dictValue = data[0]
        request.session['vendor_email'] = dictValue['ap_created_by']
        lclID = Cart.objects.count()
        status = "0"
        lclNewID = lclID + 1

        lclTotalAmt = float(request.POST['selQTY']) * float(dictValue['ap_rate']);

        Cart.objects.create (
            ct_id = lclNewID,
            ct_name = dictValue['ap_name'],
            ct_image = dictValue['ap_image'],
            ct_weight = request.POST['selQTY'],
            ct_price = dictValue['ap_rate'],
            ct_total_amount = lclTotalAmt,
            ct_ordered_by = request.session['web_email'],
            ct_status = status,
            ct_created_by = dictValue['ap_created_by'],

        )
        return HttpResponse('1')
    else:
        return HttpResponse('0')

def getCart(request):
    cart_json = Cart.objects.filter(ct_status='0', ct_ordered_by = request.session['web_email']).values()
    data = list(cart_json)
    value = JsonResponse(data, safe=False)
    return value

def cancelItem(request):
    Cart.objects.filter(ct_id = request.POST['id']).update(ct_status = "1")
    return HttpResponse()


def checkoutPayment(request):
    lclID = Order.objects.count()
    status = "0"
    lclNewID = lclID + 1

    Order.objects.create (
        or_id = lclNewID,
        or_name = request.POST['txtName'],
        or_weight = 0,
        or_rate = 0,
        or_total_amount = request.POST['totalAmt'],
        or_address = request.POST['txtAddress'],
        or_date = request.POST['txtDate'],
        or_ordered_by = request.session['web_email'],
        or_status = status,
        # or_created_by = request.session['vendor_email'],

    )

    productImage = request.POST['productImage'].split("<>")
    productQTY = request.POST['productQTY'].split("<>")
    productName = request.POST['productName'].split("<>")
    productPrice = request.POST['productPrice'].split("<>")
    productTotal = request.POST['productTotal'].split("<>")
    productVendor = request.POST['productVendor'].split("<>")
    k = 0;

    for i in productQTY:

        lclID1 = PurchasedProducts.objects.count()
        status = "0"
        lclNewID1 = lclID1 + 1

        now = datetime.datetime.now()
        dateNow = now.strftime("%Y-%m-%d")

        PurchasedProducts.objects.create (
            ps_id = lclNewID1,
            ps_or_id = lclNewID,
            ps_product_name = productName[k],
            ps_image = productImage[k],
            ps_weight = productQTY[k],
            ps_price = productPrice[k],
            ps_total_amt = productTotal[k],
            ps_date = dateNow,
            ps_status = status,
            ps_vendor_email = productVendor[k],
            ps_user_name = request.POST['txtName'],
            ps_user_email = request.session['web_email']
        )

        # product_json = Product.objects.filter(ap_name = productName[k]).values()
        # data = list(product_json)
        # dictValue = data[0]
        # print(dictValue);
        # Qty = dictValue['ap_total_quantity']

        # lclTotalQTY = int(Qty) - int(productQTY[k]);

        # Product.objects.filter(ap_name = productName[k]).update(ap_total_quantity = lclTotalQTY)
        k += 1

    return HttpResponse()

def getOrderData(request):
    if request.session['role'] == "Admin":

        getData = Order.objects.filter(or_status=1).all().values();
        jsonData = list(getData);
        return JsonResponse(jsonData, safe=False)
        return value
    else:
        products_json = Order.objects.filter(or_status = 1, or_created_by=request.session['email']).values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value

def getBuyNowURL(request):
    products_json = Product.objects.filter(ap_id=request.POST['txtID']).values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def paymentSuccess(request):
    Order.objects.filter(or_ordered_by = request.session['web_email'], or_status = "0").update(or_transaction_id = request.GET.get('transaction_id'), or_status = "1")
    Cart.objects.filter(ct_ordered_by = request.session['web_email']).update(ct_status = "1")
    return render(request, 'web/pay_success.html', {})