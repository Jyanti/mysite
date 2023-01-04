from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('signup/', views.UserView.as_view(), name = 'signup'),
    
    #path('<int:user_id>/', views.GetUserData.as_view(), name = 'fetchData'),
    
    #path('login/', views.login, name= 'login'),
    
    
    
]