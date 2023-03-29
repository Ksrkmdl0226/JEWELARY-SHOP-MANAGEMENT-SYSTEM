from atexit import register
from app import views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.openweb, name='index'),

    path("index/", views.openweb, name='index'),

    path("welcome/", views.openwelcome, name='welcome'),

    path("Aboutus/", views.aboutus, name='Aboutus'),

    path("contact/", views.contact, name='contact'),

    path("Gold/", views.Gold, name='Gold'),

    path("payment/", views.payment, name='payment'),

    path("purity/", views.purity, name='purity'),

    path("register/", views.register, name='register'),

    path("login/", views.login, name='login'),

    path("billing/", views.billing, name='bill'),

    path("shoping/", views.shoping, name='shop'),

    path("cart/", views.cart, name='cart'),

    path("check_out/", views.check, name='check'),





    # admin urls
    path("signin/", views.signin, name='signin'),

    path("adminin/", views.index1, name='admin'),

    path("admintab/", views.tables, name='tabels'),

    path("productad/", views.productad, name='productad'),

    path("cateadd/", views.cateadd, name='cateadd'),

    path("orderadd/", views.orderadd, name='orderadd'),




    # adding vendors in admin panel
    path("vendoradd/", views.vendoradd, name='vendoradd'),
    path("vendor_details/", views.vendordetail, name='vendordetails'),


    #  vendor urls
    path("vendorin/", views.vendorin, name='vendorin'),

    path("vendorad/", views.vendorindex, name='vendorad'),

    path("vendortab/", views.vendortab, name='vendortab'),

    path("vendorreg/", views.vendorreg, name='vendorreg'),

    # adding product
    path("productad1/", views.productad1, name='productad1'),
    path('product_details/', views.ProductData, name='product'),

    # category products
    path("cateadd1/", views.cateadd1, name='cateadd1'),
    path('category_details/', views.categoryDetails, name='categorydet'),

    path("orderadd1/", views.orderadd1, name='orderadd1'),

    path('admin_login_details/', views.loginAdminDetails, name='login'),
    path('check_web_login/', views.checkWebLogin, name='web_login'),
    path('add_register/', views.newRegister, name='home'),

    path('get_web_products/', views.getWebProducts, name='home'),
    path('product_details1/', views.product_details, name='home'),

    path('get_single_item/', views.getSingleItem, name='home'),

    path('check_checkout/', views.checkCheckout, name='payment'),

    path('add_cart/', views.addCart, name='cart'),

    path('get_cart/', views.getCart, name='cart'),
    path('cancel_item/', views.cancelItem, name='home'),
    path('checkout/payment/', views.checkoutPayment, name='payment'),
    path('get_buy_now_url/', views.getBuyNowURL, name='payment'),
    path('pay_success/', views.paymentSuccess, name='payment'),

    path('get_data/order/', views.getOrderData, name='order'),


    # path('book_form', views.bookForm, name='bookForm'),
 



]
