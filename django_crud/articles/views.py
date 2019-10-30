from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):

    print(request)
    print(request.path)
    print(request.method)
    print(request.headers)
    print(request.GET)
    print(request.POST)

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content)
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html') 

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # update
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article.title = title
        article.content = content
        article.save()
        return redirect("articles:detail", article.pk)
    # edit
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)