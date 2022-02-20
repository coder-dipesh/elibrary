from django.test import SimpleTestCase
from books.forms import  *


class TestForms(SimpleTestCase):
    def test_category_form(self):
        form=CategoryForm(data={
            'category_name':'Fantasy',
            'category_image':'got.png',
            'category_description':'Fantasy books',

        })
        self.assertFalse(form.is_valid())

    def test_category(self):
        form=CategoryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)  


# Testing BookForm
    def test_contact_form(self):
        form=BookForm(data={
            'book_name':'Fantasy',
            'book_author':'James Killer',
            'book_price':'5000',
            'stock':'10',
            'book_image':'got.png',
            'category':'Fantasy',

        })
        self.assertTrue(form.is_valid())

    def test_contact_form(self):
        form=BookForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),6)   

