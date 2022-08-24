from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


from store.models.customer import Customer

#Login
class Login(View):
    return_url = None
    def get (self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'store/login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password) 
            if flag:
                request.session['customer_id'] = customer.id
                # request.session['customer_email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
                
            else:
                error_message = 'Email or Password invalid!!'
                
        else:
            error_message = 'Email or Password invalid!!'
        print(email, password)
        return render (request, 'store/login.html', {'error':error_message})

def logout(request):
    request.session.clear()
    return redirect('login')