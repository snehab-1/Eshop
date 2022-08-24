from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order


class OrderView(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'store/orders.html', {'orders':orders})