from django.urls import path
from .views import Home, Article,ReadArticle
urlpatterns = [
    path('',Home.as_view()),
    path('article/',Article.as_view()),
    path('article/<int:id>',ReadArticle.as_view()),
]
