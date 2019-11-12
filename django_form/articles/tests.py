from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from .models import Article

class SettingsTest(TestCase):
    def test_01(self):
        self.assertEqual(settings.USE_I18N, True)


class BoardModelTest(TestCase):
    def test_02_model(self):
        user = User.objects.create(username="user")
        article = Article.objects.create(title="test title", content="test content", user=user)
        self.assertEqual(str(article), f'{article.title}', msg="wrong")