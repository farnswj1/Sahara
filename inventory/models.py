from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    ProhibitNullCharactersValidator
)
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=30, 
        null=False,
        unique=True,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            RegexValidator("^[A-Za-z,& ]{3,30}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    description = models.CharField(
        max_length=250, 
        null=False,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(250),
            RegexValidator(regex="^[^;]{1,250}$", message="Semicolons are not allowed."),
            ProhibitNullCharactersValidator()
        ]
    )

    def __str__(self):
        return f"Category {self.id}: {self.name}"
    
    def get_absolute_url(self):
        return reverse("inventory:category_list")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)


class Item(models.Model):
    name = models.CharField(
        max_length=50, 
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            RegexValidator("^[A-Za-z0-9,'%&:\-\.\(\) ]{2,50}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=1,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(5000)
        ]
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99_999.99)
        ]
    )
    description = models.CharField(
        max_length=250,
        null=False,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(250),
            RegexValidator(regex="^[^;]{1,250}$", message="Semicolons are not allowed."),
            ProhibitNullCharactersValidator()
        ]
    )
    quantity = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Item ID {self.id}: {self.name} (${self.price})"
    
    def get_absolute_url(self):
        return reverse("inventory:item_detail", args=(self.id,))