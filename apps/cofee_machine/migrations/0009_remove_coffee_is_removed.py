# Generated by Django 4.2.2 on 2023-06-23 18:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coffee_machine", "0008_alter_coffee_strength"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coffee",
            name="is_removed",
        ),
    ]
