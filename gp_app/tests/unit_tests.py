from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse  
from ..models import NHLTeam, Business

# Test url for the homepage/index is working
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "gp_app/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h2>Wher to Watch</h2>")
        self.assertNotContains(response, "Not on the page")

#tests that model db queries for the NHLTeams class
class NHLTeamTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.team = NHLTeam.objects.create(name = "Boston Bruins")

    def test_model_content(self):
        self.assertEqual(self.team.name, "Boston Bruins")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/nhl_team_details/", id=self.team.id)
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gp_app/index.html")
        self.assertContains(response, "<h2>Wher to Watch</h2>")

class BusinessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.biz = Business.objects.create(name = "test", email="test.mail",
            city = "test city", address = "test st.", phone_number = "1234567890")

    def tes_model_content(self):
        self.assertEqual(self.biz.name, "test")
        self.assertEqual(self.biz.email, "test.mail")
        self.assertEqual(self.biz.city, "test city")
        self.assertEqual(self.biz.address, "test st.")
        self.assertEqual(self.biz.phone_number, "1234567890")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("busniness_detail", id=self.biz.id)


