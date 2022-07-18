from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, CustomerForm, RegisterFirstLastName
from django.core.mail import send_mail
from users.models import AuthUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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
            user = form.save()
            send_mail(
                f'Welcome {user.email}',
                'We are happy to see you on our page, you can now search and save products, and change your customer settings',
                'testdjangoemailcsaba@gmail.com',
                [user.email]
            )

            login(request, user)
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
        form1 = CustomerForm()
        form2 = RegisterFirstLastName()
    else:
        form1 = CustomerForm(request.POST, instance=request.user.customer)
        form2 = RegisterFirstLastName(request.POST, instance=request.user)
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()

    return render(request, 'customer.html', {
        'form1': form1,
        'form2': form2,
    })
@login_required
def change_your_name(request):
    if request.method == 'GET':
        form2 = RegisterFirstLastName()
    else:
        form2 = RegisterFirstLastName(request.POST, instance=request.user)
        if form2.is_valid():
            form2.save()

    return render(request, 'change_name.html', {
        'form2': form2,
    })

@login_required
def change_your_details(request):
    if request.method == 'GET':
        form1 = CustomerForm()
    else:
        form1 = CustomerForm(request.POST, instance=request.user.customer)
        if form1.is_valid():
            form1.save()

    return render(request, 'change_details.html', {
        'form1': form1,
    })

@login_required
def del_user(request, user_id):
    user = get_object_or_404(AuthUser, id=user_id)
    user.delete()
    return redirect(reverse('homepage'))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('homepage'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })