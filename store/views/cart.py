from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View


from store.models.product import Product

class CartView(View):
    # def get(self, request):
    #     ids = list(request.session.get('cart').keys())
    #     print(ids)
    #     products = Product.get_products_by_id(ids)
    #     print(products)
    #     return render(request, 'store/cart.html', {'products':products})
    
    #Correct Code.....
    def get(self, request):
        cart = request.session.get('cart')
        print("cart", cart)
        if not cart:
            request.session['cart'] = {}
            ids = list(request.session.get('cart').keys())
            # products = Product.get_products_by_id(ids)
        else:
            ids = list(cart.keys())
            print("ids", ids)
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'store/cart.html', {'products':products})
    