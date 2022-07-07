from django.urls import path, include
from users.views import login_view, register_view, logout_view, customer_view, change_your_name,change_your_details, del_user, change_password
app_name = 'users'

urlpatterns = [
     path('login/', login_view, name='login'),
     path('register/', register_view, name='register'),
     path('logout/', logout_view, name='logout'),
     path('<int:user_id>/', del_user, name='delete_user'),
     path('customer/', customer_view, name='customer'),
     path('change_first_last_name/', change_your_name, name='change_first_last_name'),
     path('change_details/', change_your_details, name='change_details'),
     path('password/', change_password, name='change_password'),
]