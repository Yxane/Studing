from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women, Category

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    # return HttpResponse("Страница положения women")
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def add_page(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Логин")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'title': 'Рубрики',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Категория не найдена</h1>')
