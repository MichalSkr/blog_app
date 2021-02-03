from django.utils import timezone
from rest_framework import serializers

from .models import Writer, Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# writers
class WriterSerializer(serializers.ModelSerializer):
    articles_count = serializers.SerializerMethodField()

    def get_articles_count(self, obj):
        all_articles = Article.objects.filter(written_by=obj)
        timedelta_thirty_days = timezone.now() - timezone.timedelta(days=30)
        last_articles = \
            all_articles.filter(created_at__gte=timedelta_thirty_days)
        return {'all': all_articles.count(),
                'last': last_articles.count()}

    class Meta:
        model = Writer
        fields = ('is_editor', 'name', 'articles_count')
