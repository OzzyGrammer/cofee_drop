from django.contrib import admin
from .models import Ingredient
from .models.order import Order

# Register your models here.


@admin.register(Order)
class CoffeeAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("ingredient_mix", "add_milk", "froth_milk", "created")


@admin.register(Ingredient)
class CoffeeAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = (
        "name",
        "amount",
    )
