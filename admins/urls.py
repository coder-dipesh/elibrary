from django.urls import  path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

    path('all-orders', views.allOrders, name='all-orders'),
    path('delete-order/<int:order_id>', views.declineOrder, name='delete-order'),
    path('approve-order/<int:order_id>', views.approveOrder, name='approve-order'),



    path('all-users', views.allUsers, name='all-users'),
    path('all-admins', views.allAdmins, name='all-admins'),
    path('promote-user/<int:user_id>', views.promoteUser, name='promote-user'),
    path('delete-user/<int:user_id>', views.deleteUser, name='delete-user'),
    path('demote-admin/<int:user_id>', views.demoteAdmin, name='demote-admin'),


    path('demote-to-user/<int:user_id>', views.demoteAdmin, name='demote-to-user'),
    path('deactivate-admin/<int:user_id>', views.deactivate, name='deactivate-admin'),
    path('reactivate-admin/<int:user_id>', views.reactivate, name='reactivate-admin'),

    path('admin-change-password', views.adminChangePassword, name='admin-change-password'),

    
]
