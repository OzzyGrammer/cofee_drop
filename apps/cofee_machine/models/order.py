from django.db import models
from ..enums import Strength
from model_utils.models import TimeStampedModel
from .ingredient import Ingredient


class Order(TimeStampedModel):
    ingredient_mix = models.CharField(max_length=200, null=True, blank=True)
    strength = models.CharField(
        max_length=20,
        choices=[(s.name, s.value) for s in Strength],
        null=False,
        blank=False,
    )
    add_milk = models.BooleanField(default=False)
    froth_milk = models.BooleanField(default=False)

    def __str__(self):
        if not self.add_milk and not self.froth_milk:
            return f"coffee strength {self.strength}"
        elif self.add_milk and not self.froth_milk:
            return f"coffee strength {self.strength} with milk"
        elif self.add_milk and self.froth_milk:
            return f"coffee strength {self.strength} with milk frothed"

    @property
    def full_stock_availble(self):
        return bool()

    @property
    def coffee_cup_capacity(self):
        return 200

    @property
    def water_amount_standard_measurement(self):
        return 190

    @property
    def milk_amount_standard_measurement(self):
        return 100

    @property
    def coffee_amount_standard_measurement(self):
        return 10

    @property
    def strong_water_adjustment(self):
        return 5

    @property
    def extra_strong_coffee_adjustment(self):
        return 5

    @property
    def extra_strong_water_adjustment(self):
        return 5

    @property
    def extra_strong_coffee_adjustment(self):
        return 5

    @property
    def standard_mix_total(self):
        return (
            self.coffee_amount_standard_measurement
            + self.milk_amount_standard_measurement
            + self.water_amount_standard_measurement
        )

    def water_in_stock(self):
        try:
            water_ingredient = Ingredient.objects.get(name="Water")
            return water_ingredient
        except Ingredient.DoesNotExist:
            return None

    def coffee_in_stock(self):
        try:
            water_ingredient = Ingredient.objects.get(name="Coffee")
            return water_ingredient
        except Ingredient.DoesNotExist:
            return None

    def milk_in_stock(self):
        try:
            water_ingredient = Ingredient.objects.get(name="Milk")
            return water_ingredient
        except Ingredient.DoesNotExist:
            return None

    def has_enough_inventory(self):
        try:
            water_ingredient = Ingredient.objects.get(name="Water")
        except Ingredient.DoesNotExist:
            return None

        try:
            coffee_ingredient = Ingredient.objects.get(name="Coffee")
        except Ingredient.DoesNotExist:
            return None

        try:
            milk_ingredient = Ingredient.objects.get(name="Milk")
        except Ingredient.DoesNotExist:
            return None
        return (
            water_ingredient.amount >= self.water_amount_standard_measurement
            and coffee_ingredient.amount >= self.coffee_amount_standard_measurement
            and milk_ingredient.amount >= self.milk_amount_standard_measurement
        )

    def normal_coffee(self, strength: Strength):
        message = f"You have request to order {self.strength} strong coffee with no milk"

        try:
            water_ingredient = Ingredient.objects.get(name="Water")
        except Ingredient.DoesNotExist:
            return None

        try:
            coffee_ingredient = Ingredient.objects.get(name="Coffee")
        except Ingredient.DoesNotExist:
            return None

        if self.has_enough_inventory():
            if strength == Strength.NORMAL.name:
                water_ingredient.amount -= self.water_amount_standard_measurement
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement
                water_ingredient.save()
                coffee_ingredient.save()

                return self

            elif strength == Strength.STRONG.name:
                water_ingredient.amount -= self.water_amount_standard_measurement - 5
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement + 5
                water_ingredient.save()
                coffee_ingredient.save()

                return self

            elif strength == Strength.EXTRA_STRONG.name:
                water_ingredient.amount -= self.water_amount_standard_measurement - 10
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement + 10
                water_ingredient.save()
                coffee_ingredient.save()

                return self
        elif not self.has_enough_inventory():
            return "Not enough stock to make coffee"

    def coffee_with_milk(self, strength):
        if self.has_enough_inventory():
            try:
                water_ingredient = Ingredient.objects.get(name="Water")
            except Ingredient.DoesNotExist:
                return None

            try:
                coffee_ingredient = Ingredient.objects.get(name="Coffee")
            except Ingredient.DoesNotExist:
                return None

            try:
                milk_ingredient = Ingredient.objects.get(name="Milk")
            except Ingredient.DoesNotExist:
                return None

            if strength == Strength.NORMAL.name:
                water_ingredient.amount -= self.water_amount_standard_measurement - 100
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement
                milk_ingredient.amount -= self.milk_amount_standard_measurement
                milk_ingredient.save()
                water_ingredient.save()
                coffee_ingredient.save()

                return self

            elif strength == Strength.STRONG.name:
                water_ingredient.amount -= self.water_amount_standard_measurement - 95
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement + 5
                milk_ingredient.amount -= self.milk_amount_standard_measurement
                water_ingredient.save()
                coffee_ingredient.save()

                return self

            elif strength == Strength.EXTRA_STRONG.name:
                water_ingredient.amount -= self.water_amount_standard_measurement - 90
                coffee_ingredient.amount -= self.coffee_amount_standard_measurement + 10
                milk_ingredient.amount -= self.milk_amount_standard_measurement - 10
                water_ingredient.save()
                water_ingredient.save()
                coffee_ingredient.save()

                return self
        elif not self.has_enough_inventory():
            return "Not enough stock to make coffee"

    def brew_coffee(self):
        self.coffee_amount = self.coffee_cup_capacity
        if not self.add_milk:
            return self.normal_coffee(self.strength)
        if self.add_milk:
            return self.coffee_with_milk(self.strength)

    def save(self, *args, **kwargs):
        if not self.ingredient_mix:
            self.ingredient_mix = str(self)
        return super().save(*args, **kwargs)
