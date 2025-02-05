from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name
    

class Brands(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "brand"
        verbose_name = "Марку"
        verbose_name_plural = "Марки"

    def __str__(self) -> str:
        return self.name
    

class CarModel(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    brand = models.ForeignKey(
        to=Brands, on_delete=models.CASCADE, verbose_name="Марка"
    )

    class Meta:
        db_table = "carModel"
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self) -> str:
        return self.name
    