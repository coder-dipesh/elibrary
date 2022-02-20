from django.test import SimpleTestCase
from django.urls import reverse,resolve
from books.views import *

class TestUrls(SimpleTestCase):
    def test_category_form_urls_is_resolved(self):
      url=reverse('category-form')
      view=resolve(url).func
      self.assertEquals(view,categoryForm)
      
    def test_delete_category(self):
      url=reverse('delete-category',args=['1'])
      view=resolve(url).func
      self.assertEquals(view,deleteCategory)
      
    def test_book_form_valid(self):
      url=reverse('book-form')
      view=resolve(url).func
      self.assertEquals(view,bookForm)

    def test_book_update_form_valid(self):
      url=reverse('update-book',args=['1'])
      view=resolve(url).func
      self.assertEquals(view,bookUpdateForm)  
    
    def test_author_form_valid(self):
      url=reverse('author-form')
      view=resolve(url).func
      self.assertEquals(view,authorForm)

    def test_author_update_form_valid(self):
      url=reverse('update-author',args=['1'])
      view=resolve(url).func
      self.assertEquals(view,updateAuthor)
    
    # CART
    def test_add_to_cart_valid(self):
      url=reverse('add-to-cart',args=['1'])
      view=resolve(url).func
      self.assertEquals(view,addToCart)
      
    # View All Items
    def test_show_categories_valid(self):
      url=reverse('show-categories-user')
      view=resolve(url).func
      self.assertEquals(view,showCategories)
      














