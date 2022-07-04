from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, CustomerForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('homepage'))

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))

    return render(request, 'register.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect(reverse('homepage'))


@login_required
def customer_view(request):
    if request.method == 'GET':
        form = CustomerForm()
    else:
        form = CustomerForm(files=request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))

    return render(request, 'customer.html', {
        'form': form
    })