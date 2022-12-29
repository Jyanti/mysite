from django.urls import path

from . import views

urlpatterns = [
    path('Jyanti/', views.index, name='index'),
    path('sss', views.index, name='new_sss'),
    path('add', views.addition_two_number, name = 'addition'),
    path('add_url/<int:num1>/<int:num2>', views.addition_two_number_url, name = "addition")
]