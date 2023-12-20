from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a text!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a text!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

    def test_postpage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts.html")
