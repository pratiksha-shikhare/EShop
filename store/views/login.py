from django.views import View
from django.shortcuts import render, redirect,HttpResponseRedirect
# from store.models.product import Product
# from store.models.category import Category
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        print('Data is: ',email,password,customer)
        print(customer.id)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer']=customer.id
                # request.session['customer_email']=customer.email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password is invalid !!'
        else:
            error_message = 'Customer with email is not Exist !!'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
