from django.urls import path


from .views import Index, Signup, Login, CartView, CheckOut, OrderView
from .views.login import logout
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', CartView.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checko-out'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders')
]