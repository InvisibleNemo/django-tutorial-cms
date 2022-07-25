from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.

class LandingPageTest(TestCase):
    
    def test_status_code(self):
        #TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
                
        # print(response.content)
        # print(response.status_code)
        # pass
    
    def test_template_name(self):
        #TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        self.assertTemplateUsed(response, "landing.html")
    
    
    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")