from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_category_form_get(self):
        client=Client()
        response=client.get(reverse('category-form'))
        self.assertTemplateUsed(response,'books/categoryForm.html')

    def test_get_book(self):
        client=Client()
        response=client.get(reverse('get-book'))
        self.assertTemplateUsed(response,'books/getBook.html')



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        