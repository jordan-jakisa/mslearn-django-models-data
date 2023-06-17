from django.db import models


class Shelter(models.Model):
    name = models.TextField(max_length=200)
    location = models.CharField(max_length=200)

    # dog_set field will be automatically created

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    intake_date = models.DateTimeField(auto_now_add=True)

    shelter = models.ForeignKey(
        Shelter,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
# Create your models here.

# class Product(models.Model):
#     name = models.TextField(max_length=50, min_lenght=3, unique=True)  # field
#     price = models.DecimalField(min_value=0.99, max_value=1000)
#     creation_date = models.DateField(auto_now_add=True)  # parenthesis values are field options
#
#     category = models.ForeignKey(
#         'Catergory',
#         on_delete=models.PROTECT
#         # PROTECT throws an error when parent is deleted
#         # while CASCADE deletes all products when a parent has been deleted
#     )
#
#     # def __str__(self):  # generic method
#     #   return self.name
#     #   pass
#
#
# class Category(models.Model):
#     name = models.TextField(max_length=50, min_lenght=5, unique=True)
#     #product_set or <child>_set will be automatically added
