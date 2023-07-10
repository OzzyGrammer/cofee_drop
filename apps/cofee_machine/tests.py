from django.test import TestCase
from .enums import Strength
from .models import Order


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order(
            strength=Strength.NORMAL.name, add_milk=False, froth_milk=False
        )

    def test_str_representation(self):
        expected_str = "coffee strength NORMAL"
        self.assertEqual(str(self.order), expected_str)

    def test_has_enough_inventory_with_enough_stock(self):
        # Assume there is enough stock of water, coffee, and milk
        self.assertTrue(self.order.has_enough_inventory())

    def test_has_enough_inventory_without_enough_stock(self):
        # Assume there is not enough stock of water, coffee, or milk
        self.assertFalse(self.order.has_enough_inventory())

    def test_normal_coffee_with_enough_inventory(self):
        # Assume there is enough stock of water and coffee
        result = self.order.normal_coffee(Strength.NORMAL.name)
        self.assertEqual(result, self.order)

    def test_normal_coffee_without_enough_inventory(self):
        # Assume there is not enough stock of water or coffee
        result = self.order.normal_coffee(Strength.NORMAL.name)
        self.assertEqual(result, "Not enough stock to make coffee")

    def test_coffee_with_milk_with_enough_inventory(self):
        # Assume there is enough stock of water, coffee, and milk
        result = self.order.coffee_with_milk(Strength.NORMAL.name)
        self.assertEqual(result, self.order)

    def test_coffee_with_milk_without_enough_inventory(self):
        # Assume there is not enough stock of water, coffee, or milk
        result = self.order.coffee_with_milk(Strength.NORMAL.name)
        self.assertEqual(result, "Not enough stock to make coffee")

    def test_brew_coffee_without_milk(self):
        # Assume there is enough stock of water and coffee
        result = self.order.brew_coffee()
        self.assertEqual(result, self.order.normal_coffee(Strength.NORMAL.name))

    def test_brew_coffee_with_milk(self):
        # Assume there is enough stock of water, coffee, and milk
        self.order.add_milk = True
        result = self.order.brew_coffee()
        self.assertEqual(result, self.order.coffee_with_milk(Strength.NORMAL.name))
