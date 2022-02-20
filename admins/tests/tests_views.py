from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_adminDashboard_get(self):
        client=Client()
        response=client.get(reverse('dashboard'))
        self.assertTemplateUsed(response,'admins/dashboard.html')

    def test_all_users_get(self):
        client=Client()
        response=client.get(reverse('all-users'))
        self.assertTemplateUsed(response,'admins/allUsers.html')

    def test_get_all_admins_get(self):
        client=Client()
        response=client.get(reverse('all-admins'))
        self.assertTemplateUsed(response,'admins/allAdmins.html')
    
    def test_get_allorders_get(self):
        client=Client()
        response=client.get(reverse('all-orders'))
        self.assertTemplateUsed(response,'admins/allOrders.html')



