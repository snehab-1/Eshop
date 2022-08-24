from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


from store.models.customer import Customer


#signup
class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')
        
        #validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'email': email
        }
        error_message = None
        
        customer = Customer(first_name = first_name, last_name = last_name, mobile = mobile, 
                    email = email, password = password)
        
        error_message = self.validateCustomer(customer)
            
        #saving
        if not error_message:
            print(first_name, last_name, mobile, email, password)
            customer.password = make_password(customer.password)
            # customer.save()
            customer.register()
            # return HttpResponseRedirect("/")
            return redirect("home")
        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request, 'store/signup.html', data)
    
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First name is required"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 chr long or more"
        elif (not customer.last_name):
            error_message = "Last name is required"
        elif len(customer.last_name) < 4:
            error_message = "Last name must be 4 chr long or more"
        elif (not customer.mobile):
            error_message = "Mobile no is required"
        elif len(customer.mobile) < 10:
            error_message = "Mobile no must be 10 digit"
        elif (not customer.email):
            error_message = "Email name is required"
        elif len(customer.email) < 8:
            error_message = "Email must be 10 digit"
        elif (not customer.password):
            error_message = "Password name is required"
        elif len(customer.mobile) < 8:
            error_message = "Password must be 8 digit"
        elif customer.isExists():
            error_message = "Email Address Already Registered"
    
        return error_message