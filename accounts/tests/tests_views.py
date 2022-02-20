from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_homepage(self):
        client=Client()
        response=client.get(reverse('homepage'))
        self.assertTemplateUsed(response,'accounts/homepage.html')

    def test_signin(self):
        client=Client()
        response=client.get(reverse('signin'))
        self.assertTemplateUsed(response,'accounts/signin.html')

    def test_signup(self):
        client=Client()
        response=client.get(reverse('signup'))
        self.assertTemplateUsed(response,'accounts/signup.html')
        
        
    def  test_contactUs(self):
        client=Client()
        response=client.get(reverse('contact-us'))
        self.assertTemplateUsed(response,'accounts/contactUs.html')

    