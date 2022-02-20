from django.test import SimpleTestCase
from django.urls import reverse,resolve
from admins.views import *

class TestUrls(SimpleTestCase):
    def test_admin_dashboard_urls_is_resolved(self):
      url=reverse('dashboard')
      view=resolve(url).func
      self.assertEquals(view,dashboard)

    def test_all_orders_urls_is_resolved(self):
      url=reverse('all-orders')
      view=resolve(url).func
      self.assertEquals(view,allOrders)

    def test_all_users_urls_is_resolved(self):
      url=reverse('all-users')
      view=resolve(url).func
      self.assertEquals(view,allUsers)
    
    def test_all_admins_urls_is_resolved(self):
      url=reverse('all-admins')
      view=resolve(url).func
      self.assertEquals(view,allAdmins)
    
    def test_decline_order_urls_is_resolved(self):
      url=reverse('delete-order',args=[1])
      view=resolve(url).func
      self.assertEquals(view,declineOrder)

    def test_approve_order_urls_is_resolved(self):
      url=reverse('approve-order',args=[1]) 
      view=resolve(url).func
      self.assertEquals(view,approveOrder)

    
    def test_demote_to_users_urls_is_resolved(self):
      url=reverse('demote-to-user',args=[1])
      view=resolve(url).func
      self.assertEquals(view,demoteAdmin)








