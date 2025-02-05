from django.urls import path
from cars import views

app_name = "cars"

urlpatterns = [
    path('rent/', views.rent, name='rent'),
    # path('get-brands/<int:category_id>/', views.get_brands, name='get_brands'),
]
