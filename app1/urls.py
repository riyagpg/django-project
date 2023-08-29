from django.urls import path
from app1.views import *

urlpatterns = [
    path('',index,name="home"),
    path('all-product/',allproduct,name="all_product"),
    path('filter-product/<int:id>/',product_filter,name="filter_product"),
    path('get-product/<int:id>/',product_get,name="get_product"),
    path('User-register/',Register,name="register"),
    path('login/',login,name="login1"),
    path('logout/',logout,name="logout1"),
    path('buynow/',buynow,name="buynow1"),
    path('My Order/',myorder,name='myorder'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('successview/',sucess,name="orderSuccessView"),
]