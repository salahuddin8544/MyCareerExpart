import random

from rest_framework.reverse import reverse

from home.base_tests import BaseTestCase

from django.utils import timezone

class AuthUserLoginAPITest(BaseTestCase):
    
    def setUp(self):
        self.url = reverse('rest_login')
        super().setUp()
        
    def test_authentication(self):
             
        # =================================
        # Test login
        # =================================
        
        # login
        login = self.client.login(email='johndoe@example.com', password='testpass')
        self.loginSeccess(login)
        
        # logout        
        self.client.logout()