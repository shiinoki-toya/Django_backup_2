from django.urls import path
from . import views
from .views import DetailView
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('lists/', views.lists, name='lists'),
    path('select/', views.select, name='select'),

    path('detail/', DetailView.as_view(), name='detail'),
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
]