from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from datetime import datetime

from .models import ArticleModel
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'index.html',{})
    def post(self,request):
        return HttpResponse('<h1>Hellow there...</h1>')


class Article(View):
    def get(self,request):
        # posts=[{
        #     "title":"The First Article",
        #     "author": "Sanzid Olioul Tanzid",
        #     "date": datetime.now(),
        #     "blog":"Hii there , it is my first django project . I am trying to use the app form scratch.",
        # },
        # {
        #     "title":"The Secound Article",
        #     "author": "Sanzid Olioul Tanzid",
        #     "date": datetime.now(),
        #     "blog":"Hii there , it is my first django project . I am trying to use the app form scratch. And trying to make my life better...",
        # }
        #]

        posts = ArticleModel.objects.all()
        
        return render(request,'blogs.html',{"posts":posts})
    def post(self,request):
        title = request.POST['title']
        author = request.POST['author']
        post = request.POST['post']
        time_created = datetime.now()
        ArticleModel.objects.create(title = title , author = author,post = post,time_created=time_created)
        return redirect('/blog/article')


class ReadArticle(View):
    def get(self,request,id):
        article = ArticleModel.objects.get(id = id)
        return render(request,'spacific.html',{"post" : article})