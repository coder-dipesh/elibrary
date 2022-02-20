from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import *

class TestUrls(SimpleTestCase):
    def test_homepage_urls_is_resolved(self):
      url=reverse('homepage')
      view=resolve(url).func
      self.assertEquals(view,homepage)
      
    def test_signin_urls_is_resolved(self):
      url=reverse('signin')
      view=resolve(url).func
      self.assertEquals(view,signin)
      
    def test_signup_urls_is_resolved(self):
      url=reverse('signup')
      view=resolve(url).func
      self.assertEquals(view,signup)
    
    def test_signout_urls_is_resolved(self):
      url=reverse('signout')
      view=resolve(url).func
      self.assertEquals(view,signout) 
      
    def test_getProfile_urls_is_resolved(self):
      url=reverse('user-profile')
      view=resolve(url).func
      self.assertEquals(view,getProfile)
      
    def test_updateUserProfile_urls_is_resolved(self):
      url=reverse('update-user-profile')
      view=resolve(url).func
      self.assertEquals(view,updateUserProfile)
      
    def test_changePassword_urls_is_resolved(self):
      url=reverse('change-password')
      view=resolve(url).func
      self.assertEquals(view,changePassword)      
  
    def test_contactUs_urls_is_resolved(self):
      url=reverse('contact-us')
      view=resolve(url).func
      self.assertEquals(view,contactUs)
    
    
   
   
   
   
   
   
   
   
   