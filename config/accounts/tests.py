from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse

class MessageTest(SimpleTestCase):
    def test_url_exist(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)
        
    def test_url_avaliable_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)    
    
    def test_template_name(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response,'registration/signup.html')
    def test_content_name(self):
        response = self.client.get('/accounts/signup/')
        self.assertContains(response,'<h1>Sign UP Form</h1>')