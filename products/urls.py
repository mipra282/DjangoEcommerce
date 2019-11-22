from django.urls import path
from django.contrib.auth.views import login,logout
from products.views import products_view

urlpatterns = [
    path('', products_view),
    path(r'login', login,{'template_name': 'accounts/login.html'}, name='login'),
    path(r'^logout/$', logout, name='logout'),

]