from django.test import TestCase
from django.test import Client
from django.urls import reverse
from assignments.models import Assignment


class TestAssignment(TestCase):
    def setUp(self):
        self.client = Client()
        self.assignment = Assignment()
        self.assignment.candidate = "John Smith"
        self.assignment.position = "Python Developer"
        self.assignment.email = "test@test.com"
        self.assignment.dropbox_id = ""
        self.assignment.save()

    def testDown(self):
        Assignment.objects.all().delete()

    def test_index_returns_200(self):
        response = self.client.get(reverse("assignment-home"))
        self.assertEquals(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_show_returns_200(self):
        response = self.client.get(
            reverse("assignment-show", args=[self.assignment.pk])
        )
        self.assertEquals(response.status_code, 200)

    def test_show_template(self):
        response = self.client.get(
            reverse("assignment-show", args=[self.assignment.pk])
        )
        self.assertTemplateUsed(response, "show.html")

    def test_new_returns_200(self):
        response = self.client.get(reverse("assignment-new"))
        self.assertEquals(response.status_code, 200)

    def test_new_template(self):
        response = self.client.get(reverse("assignment-new"))
        self.assertTemplateUsed(response, "new.html")
