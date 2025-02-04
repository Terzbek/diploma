from django.shortcuts import render


def index(request):
    context = {
        "title": "Car24 - Home page",
    }
    return render(request, "main/index.html", context)


def test(request):
    return render(request, 'main/test2.html')
