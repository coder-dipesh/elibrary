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


    def test_show_all_orders(self):
        client=Client()
        response=client.get(reverse('user-all-order'))
        self.assertTemplateUsed(response,'books/userAllOrder.html')
        
        
    def test_show_all_books(self):
        client=Client()
        response=client.get(reverse('show-books-user'))
        self.assertTemplateUsed(response,'books/showBooks.html')
        
        
    def test_show_all_authors(self):
        client=Client()
        response=client.get(reverse('show-authors-user'))
        self.assertTemplateUsed(response,'books/showAuthors.html')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        