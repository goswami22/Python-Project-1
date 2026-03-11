from django.shortcuts import render, redirect
from . models import Contact, User, Product1, Wishlist, Cart
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.mail import send_mail
from django.conf import settings
import requests
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import stripe


YOUR_DOMAIN = 'http://localhost:8000'
stripe.api_key = settings.STRIPE_PRIVATE_KEY

# Create your views here.

def index(request):
    try:
        user=User.objects.get(email=request.session['email'])
        if user.usertype =='buyer':
            return render(request, 'index.html')
        else:
            return render(request, 'seller-index.html')
    except:
         return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message']
        )
        msg="Contact Saved Successfully"
        return render(request, 'contact.html',{'msg':msg})
    else:
         if request.session.get('email'):
            user=User.objects.get(email=request.session['email'])
            if user.usertype=='buyer':
                return render(request, 'index.html')
            else:
                return render(request, 'seller-index.html')
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        try:
            User.request.get(email=request.POST['email'])
            msg="Email is already registered"
            return render(request, 'login.html', {'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    address=request.POST['address'],
                    profile_pricture=request.FILES['profile_pricture'],
                    usertype=request.POST['usertype']
                )
                msg='User sign up Successfully'
                return render(request, 'login.html', {'msg':msg})        
            else:
                msg="Password and Confirm passwoed does not match"
                return render(request, 'signup.html', {'msg':msg})       
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        try:
            user= User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_pricture']=user.profile_pricture.url
                if user.usertype=='buyer':
                    wishlists=Wishlist.objects.filter(user=user)
                    request.session['wishlist_count']=len(wishlists)
                    # for cart
                    carts=Cart.objects.filter(user=user,payment_status=False)
                    request.session['cart_count']=len(carts)
                    return render(request,'index.html')
                else:
                    return render(request,'seller-index.html')
            else:
                msg='Incorrect password'
                return render(request, 'login.html', {'msg':msg})
        except:
            msg = 'Email not registered'
            return render(request, 'login.html', {'msg':msg})    
    else:    
        return render(request, 'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_pricture']
        del request.session['wishlist_count']
        del request.session['cart_count']
        msg = "Logout successfully"
        return render(request, 'login.html', {'msg':msg})
    except:
        msg = "Logout successfully"
        return render(request, 'login.html', {'msg':msg})
    
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method== 'POST':
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.email=request.POST['email']
        user.address=request.POST['address']
        user.mobile=request.POST['mobile']
        try:
            user.profile_pricture=request.FILES['profile_pricture']
        except:
            pass
        user.save()
        request.session['profile_pricture']=user.profile_pricture.url
        msg="Profile Updated successfully"
        if user.usertype == 'buyer':
            return render(request, 'profile.html', {'user':user, 'msg':msg})
        else:
            return render(request, 'seller-profile.html', {'user':user, 'msg':msg})
    else:  
        if user.usertype =='buyer':  
            return render(request, 'profile.html', {'user':user})
        else:
            return render(request, 'seller-profile.html', {'user':user})

def my_account(request):
    user = User.objects.get(email=request.session['email'])

    if request.method == 'POST':
        user.fname = request.POST['fname']
        user.address = request.POST['address']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        user.save()

    return render(request, 'my-account.html', {'user': user})

def forgot_password(request):
    if request.method == 'POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000, 9999)
            subject='OTP for forgot password'
            message='Your otp forgot pasword is '+str(otp)
            send_mail(subject, message,settings.EMAIL_HOST_USER,[user.email,])
            request.session["otp"]=otp
            request.session['to_email']=user.email
            return render(request, 'otp.html')
        except:
            msg='Email not registred'
            return render(request, 'forgot-password.html', {'msg':msg})
    else:
         return render(request, 'forgot-password.html')

def verify_otp(request):
    otp1=int(request.POST['otp'])
    otp2=int(request.session['otp'])

    if otp1 == otp2:
        del request.session['otp']
        msg='Set your new password'
        return render(request, 'new-password.html', {'msg':msg})
    else:
        msg='Invalid OTP'
        return render(request, 'otp.html')

def new_password(request):
    if request.POST['new_password']==request.POST['confirm_password']:
        user=User.objects.get(email=request.session['to_email'])
        if user.password!=request.POST['new_password']:
            user.password=request.POST['new_password']
            user.save()

            del request.session['to_email']
            msg='Password Update Successfully'
            return render(request, 'login.html',{'msg':msg})
        else:
            msg='Your new password cannot your old password'  
            return render(request, 'new-password.html',{'msg':msg})
    else:
        msg='Your new password & confirm password dosenot match'  
        return render(request, 'new-password.html',{'msg':msg})
    

def seller_add_product(request):
    seller=User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Product1.objects.create(
            seller=seller,
            product_category=request.POST['product_category'],
            product_name=request.POST['product_name'],
            product_price=request.POST['product_price'],
            product_desc=request.POST['product_desc'],
            profile_pricture=request.FILES['profile_pricture'],
        )
        msg='Product added Successfully'
        return render(request, 'seller-add-product.html', {'msg':msg})
    else:
        return render(request, 'seller-add-product.html')

def seller_view_product(request):
    seller=User.objects.get(email=request.session['email'])
    products=Product1.objects.filter(seller=seller)
    return render(request,'seller-views-product.html',{'products':products})

def seller_product_details(request,pk):
    product=Product1.objects.get(pk=pk)
    return render(request, 'seller-product-details.html',{'product': product})


def seller_edit_product(request, pk):
    product=Product1.objects.get(pk=pk)
    if request.method == 'POST':
        product.product_category=request.POST['product_category']
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_desc=request.POST['product_desc']
        try:
            product.profile_pricture=request.FILES['profile_pricture']
        except:
            pass
        product.save()
        return redirect('seller-view-product')
    else:
        return render(request, 'seller-edit-product.html', {'product': product})



def seller_delete_product(request, pk):
    product=Product1.objects.get(pk=pk)
    product.delete()
    return redirect('seller-view-product')

def seller_account(request):
    return render(request, 'seller-account.html')

def products(request):
    all_products=Product1.objects.all()
    return render(request, 'products.html', {'all_products':all_products})

def product_details(request, pk):
    wishlist_flag = False
    cart_flag = False
    product=Product1.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    try:
        Wishlist.objects.get(user=user, product=product)
        wishlist_flag = True
    except:
        pass    
    try:
        Cart.objects.get(user=user, product=product,payment_status=False)
        cart_flag = True
    except:
        pass    
    return render(request, 'product-details.html', {'product':product,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})


def add_to_wishlist(request, pk):
    product=Product1.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(user=user, product=product)
    return redirect('wishlist')

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user)
    request.session['wishlist_count']=len(wishlists)
    return render(request, 'wishlist.html',{'wishlists':wishlists})

def remove_form_wishlist(request,pk):
    product=Product1.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

def add_to_cart(request, pk):
    product=Product1.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(user=user, product=product, product_price=product.product_price,product_qut=1,total_price=product.product_price,payment_status=False)
    return redirect('cart')

def cart(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status=False)
    for i in carts:
        net_price=net_price + i.total_price
    request.session['cart_count']=len(carts)
    return render(request, 'cart.html',{'carts':carts,'net_price':net_price })

def remove_form_cart(request,pk):
    product=Product1.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart')

# Sir content

# def change_qty(request):
#     pk=int(request.POST['id'])
#     product_qut=int(request.POST['product_qut'])
#     cart=Cart.objects.get(pk=pk)
#     cart.product_qut=product_qut
#     cart.total_price=cart.product_price * product_qut
#     cart.save()
#     return redirect('cart')


def change_qty(request):
    pk = int(request.POST['id'])
    action = request.POST['action']

    cart = Cart.objects.get(pk=pk)

    if action == "increase":
        cart.product_qut += 1

    elif action == "decrease":
        if cart.product_qut > 1:
            cart.product_qut -= 1

    cart.total_price = cart.product_price * cart.product_qut
    cart.save()

    return redirect('cart')

@csrf_exempt
def create_checkout_session(request):
	amount = int(json.load(request)['post_data'])
	final_amount=amount*100
	user=User.objects.get(email=request.session['email'])
	user_name=f"{user.fname} {user.lname}"
	user_address=f"{user.address}"
	user_mobile=f"{user.mobile}"
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'unit_amount': final_amount,
				'product_data': {
					'name': 'Checkout Session Data',
					'description':f'''Customer:{user_name},\n\n
					Address:{user_address},\n
					Mobile:{user_mobile}''',
				},
			},
			'quantity': 1,
			}],
		mode='payment',
		success_url=YOUR_DOMAIN + '/success.html',
		cancel_url=YOUR_DOMAIN + '/cancel.html',
		customer_email=user.email,
		shipping_address_collection={
			'allowed_countries':['IN'],
		}
		)
	return JsonResponse({'id': session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts:
		i.payment_status=True
		i.save()
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html')

def cancel(request):
	return render(request,'cancel.html')
def myorders(request):
    user=User.objects.get(email=request.session['email'])
    orders=Cart.objects.filter(user=user,payment_status=True)
    return render(request, 'my-orders.html', {'orders':orders})