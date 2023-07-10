from django.db import models
from ..enums import Strength
from model_utils.models import TimeStampedModel

# Create your models here.


class Ingredient(TimeStampedModel):
    """
    Model representing an ingredient.

    Each ingredient has a name and an amount.
    """

    name = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        max_length=200,
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        Return a string representation of the ingredient.

        The string representation is the name of the ingredient.
        """
        return self.name
