from django.urls import path

from . import views

urlpatterns = [
    path('', views.Summary.as_view(), name='blog_app_summary'),
    path('article/', views.ArticleAdd.as_view()),
    path('article-approval/', views.ArticleApproval.get_new),
    path('article-approval/<int:article_id>/',
         views.ArticleApproval.update_article),
    path('articles-edited/', views.ArticleApproval.get_all),
]
