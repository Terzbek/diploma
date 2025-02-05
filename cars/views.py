from django.http import JsonResponse
from django.shortcuts import render
from cars.models import Categories, Brands, CarModel


def rent(request):
    categories = Categories.objects.all() # select * from categories
    brands = Brands.objects.all()

    context = {
        # "title": "car24 - rent page",
        "categories": categories,
        "brands": brands,
    }

    return render(request, 'cars/rent.html', context)

def get_brands(request, category_id):
    category_id = category_id
    brands = Brands.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(brands), safe=False)
