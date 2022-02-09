from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signin', views.signin, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),

    path('user_profile', views.get_profile, name='user_profile'),
    path('update_user_profile', views.update_user_profile, name='update_user_profile'),

    path('change_password', views.change_password, name='change_password'),

    
]
