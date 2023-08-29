from django.shortcuts import render,redirect
# from app1.models import Category,Userregister,Product,Order
from django.http import HttpResponse
from app1.models import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.

def index(request):
    data=Category.objects.all()
    
    return render(request,'index.html',{'cat':data})


def allproduct(request):
    data=Product.objects.all()
    return render(request,'product.html',{'cat':data})



def product_filter(request,id):
    data=Product.objects.filter(categoryname=id)
    return render(request,'product.html',{'cat':data})

def product_get(request,id):
    if 'm' in request.session:
        m=request.session['m']
        del request.session['m']
    else:
        m=""
    data=Product.objects.get(id=id)
    return render(request,'product_details.html',{'cat':data,"m":m})

def Register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        address1=request.POST['address']
        number1=request.POST['number']
        pass1=request.POST['password']
        userdata=Userregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        if len(Userregister.objects.filter(email=email1))==0:
            userdata.save()
            return redirect('login1')
        else:
            return render(request,'register.html',{'m':"User Already Exist"})
    return render(request,'register.html')


def login(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user=Userregister.objects.get(email=email1,password=password1)
            if user:
                request.session['id']=user.pk
                request.session['email']=user.email
                return redirect('home')
            else:
                return render(request,'login.html',{'m':'Invalid password'})
        except:
            return render(request,'login.html',{'m':'Invalid Data Enter'})
    return render(request,'login.html')

def logout(request):
    if "email" in request.session:
        del request.session['id']
        del request.session['email']
        return redirect('login1')
    else:
        return redirect('login1')
    

def buynow(request):
    if "email" in request.session:
        if request.POST:
            x=request.POST['productid']
            productdata=Product.objects.get(id=x)
            if int(productdata.quantity) >= int(request.POST['quantity']):
                request.session['productid']=x
                request.session['quantity']=request.POST['quantity']
                request.session['price']=int(request.POST['quantity'])*int(productdata.price)
                request.session['paymentmethod']="Razorpay"
                return redirect('razorpayView')
            else:
                request.session['m']="Quantity not available left only {}".format(productdata.quantity)
                return redirect("get_product",x)
    else:
        return redirect('login1') 



def myorder(request):
    if "email" in request.session:
        orderdata=Order.objects.filter(userid=request.session['id'])
        prolist=[]
        for i in orderdata:
            pro={}
            productdata=Product.objects.get(id=i.productid)
            pro['img']=productdata.img
            pro['name']=productdata.name
            pro['quantity']=i.quantity
            pro['price']=i.paymentamt
            pro['transactionid']=i.transactionid
            pro['date']=i.datetime
            prolist.append(pro)
        return render(request,'ordertable.html',{'list':prolist})
    else:
        return redirect('login1')

def sucess(request):
    if "email" in request.session:
        return render(request,'order_sucess.html')
    else:
        return redirect('login1')



RAZOR_KEY_ID = 'rzp_test_7vDl5AqMrqQGEC'
RAZOR_KEY_SECRET = 'ngzVbY2jpdmNKhmqafwn2nt1'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['price'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['price'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = Order()
            orderModel.userid=request.session['id']
            orderModel.productid=request.session['productid']
            orderModel.quantity=request.session['quantity']
            orderModel.paymentamt = request.session['price']
            orderModel.paymentmethod = request.session['paymentmethod']
            orderModel.transactionid = payment_id
            productdata=Product.objects.get(id=request.session['productid'])
            productdata.quantity-=int(request.session['quantity'])
            productdata.save()
            orderModel.save()            
            del request.session['productid']
            del request.session['quantity']
            del request.session['price']
            del request.session['paymentmethod']
            return redirect('orderSuccessView')
            
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()