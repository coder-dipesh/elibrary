from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),

    path('user-profile', views.getProfile, name='user-profile'),
    path('update-user-profile', views.updateUserProfile, name='update-user-profile'),

    path('change-password', views.changePassword, name='change-password'),

    path('contact-us', views.contactUs, name='contact-us'),


    
]
