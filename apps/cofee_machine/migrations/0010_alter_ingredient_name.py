# Generated by Django 4.2.2 on 2023-06-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coffee_machine", "0009_remove_coffee_is_removed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
