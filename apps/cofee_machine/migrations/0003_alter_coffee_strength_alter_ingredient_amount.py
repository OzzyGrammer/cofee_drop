# Generated by Django 4.2.2 on 2023-06-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "coffee_machine",
            "0002_remove_coffee_ingredient_coffee_ingredient_mix_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee",
            name="strength",
            field=models.CharField(
                blank=True,
                choices=[("NORMAL", 1), ("STRONG", 2), ("EXTRA_STRONG", 3)],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, max_length=200, null=True
            ),
        ),
    ]