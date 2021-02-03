from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Writer, Article
from .forms import WriterArticleForm
from .serializers import WriterSerializer, ArticleSerializer


class ArticleAdd(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        form = WriterArticleForm()
        return render(request, 'article_detail.html', {'form': form})

    @staticmethod
    def post(request):
        current_user = request.user
        post_values = request.POST.copy()
        post_values['written_by'] = current_user.id
        form = WriterArticleForm(post_values)

        if form.is_valid():
            note = form.save(commit=False)
            note.written_by = current_user
            note.save()
            return HttpResponseRedirect('..')


# Articles summary
class Summary(APIView):

    @staticmethod
    def get(request):
        writers = Writer.objects.all()
        if not writers:
            return Response(status=404)
        else:
            serialized_writers = WriterSerializer(writers, many=True).data
            return render(request, 'writers.html',
                          {'writers': serialized_writers})


# Articles approval
class ArticleApproval(APIView):

    @staticmethod
    def get_new(request):
        articles = Article.objects.filter(edited_by=request.user.id,
                                          approve_reject='')
        if not articles:
            return redirect('/admin')
        else:
            serialized_articles = ArticleSerializer(articles, many=True).data
            return render(request, 'article_approval.html',
                          {'articles': serialized_articles})

    @staticmethod
    def get_all(request):
        articles = Article.objects.filter(edited_by=request.user.id)
        if not articles:
            return redirect('/admin')
        else:
            serialized_articles = ArticleSerializer(articles, many=True).data
            return render(request, 'article_all.html',
                          {'articles': serialized_articles})

    @staticmethod
    def update_article(request, article_id):
        article = Article.objects.get(id=article_id)
        action_type = request.POST.get('action_type', '')
        if action_type:
            article.approve_reject = action_type
            article.save()
            return HttpResponse('success')
        return HttpResponse('')
