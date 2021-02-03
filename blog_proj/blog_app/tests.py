from django.test import TestCase, Client
from django.utils import timezone

from .models import Writer, Article


class TestViewsAll(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.client = Client()

    def test_empty_summary_get(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 404)

    def test_article_add_unauthorized(self):
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 403)


class TestViewsUser(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.client = Client()
        writer = Writer.objects.create_user(name='jacob',
                                            password='top_secret',
                                            is_staff=True)
        Article.objects.create(title='test',
                               written_by=writer,
                               edited_by=writer)
        creation_at = timezone.now() - timezone.timedelta(days=31)
        Article.objects.create(title='test',
                               written_by=writer,
                               edited_by=writer,
                               created_at=creation_at)
        self.client.login(name='jacob', password='top_secret')

    def test_articles_summary_user(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'writers.html')

    def test_articles_summary_number(self):
        response = self.client.get('')
        articles_count = response.context.get('writers')[0] \
            .get('articles_count')
        self.assertEqual(articles_count.get('all'), 2)
        self.assertEqual(articles_count.get('last'), 1)

    def test_articles_get_all(self):
        response = self.client.get('/articles-edited/')
        self.assertTemplateUsed(response, 'article_all.html')
        self.assertEqual(len(response.context.get('articles')), 2)
