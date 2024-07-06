from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .forms import EmailForm


def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmailForm()
    return render(request, 'main/index.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Hello, world. You're at the categories index.</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Hello, world. You're at the categories index.</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2024:
        raise Http404("Hato yil kiritildi")

    return HttpResponse(f"<h1>You're at the archive index.</h1><p>year: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>sayt topilmadi</h1>")
