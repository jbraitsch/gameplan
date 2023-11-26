from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse  
from .models import NHLTeam
from django.contrib.auth.models import User

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

class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username = "test", email="jbraitsc@uccs.edu", password = "4rfvbgt5")

    def tes_model_content(self):
        self.assertEqual(self.user.username, "test")
        self.assertEqual(self.user.email, "jbraitsc@uccs.edu")
        self.assertEqual(self.user.password, "4rfvbgt5")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")


