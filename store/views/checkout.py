from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        customer = request.session.get('customer_id')
        # print(customer, mobile, address, cart, products)
        
        for product in products:
            order = Order(customer = Customer(id=customer), product=product, price=product.price, 
                          address=address, mobile=mobile, quantity=cart.get(str(product.id)))
            
            order.placeOrder()
            
        request.session['cart'] = {}
        
        return redirect('cart')