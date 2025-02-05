from django.contrib import admin


from cars.models import CarModel, Categories, Brands

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
