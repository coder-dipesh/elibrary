from django.test import SimpleTestCase
from accounts.forms import  *


class TestForms(SimpleTestCase):
    def test_profile_form(self):
        form=ProfileForm(data={
            'user':'johndoe',
            'forget_password_token':'12345',
            'firstname':'John',
            'lastname':'Doe',
            'username':'eLibrary.user',
            'email':'johndoe@gmail.com',
            'phone':'9816034112',
            'address':'Buddanilakantha',
            'city':'Kathmandu',
            'profile_pic':'user.png',

        })
        self.assertTrue(form.is_valid())

    def test_profile_form(self):
        form=ProfileForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertNotEquals(len(form.errors),8)   

    def test_contact_form(self):
        form=ContactForm(data={
            'name':'johndoe',
            'email':'johndoe@gmail.com',
            'message':'Hello how can i get service.',

        })
        self.assertTrue(form.is_valid())

    def test_contact_form(self):
        form=ContactForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertNotEquals(len(form.errors),8)   
    


