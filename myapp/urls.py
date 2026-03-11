from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('my-account/',views.my_account, name='my-account'),
    path('forgot-password/',views.forgot_password, name='forgot-password'),
    path('verify-otp/',views.verify_otp, name='verify-otp'),
    path('new-password/',views.new_password, name='new-password'),
    path('seller-add-product/',views.seller_add_product, name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product, name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details, name='seller-product-details'),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product, name='seller-edit-product'),
    path('seller-delete-product/<int:pk>/',views.seller_delete_product, name='seller-delete-product'),
    path('products/',views.products, name='products'),
    path('product-details/<int:pk>/',views.product_details, name='product-details'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('remove-form-wishlist/<int:pk>/',views.remove_form_wishlist, name='remove-form-wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.cart, name='cart'),
    path('remove-form-cart/<int:pk>/',views.remove_form_cart, name='remove-form-cart'),
    path('change-qty/',views.change_qty, name="change-qty"),
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
    path('myorders/', views.myorders,name='myorders'),
]

