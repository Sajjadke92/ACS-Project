# Generated by Django 5.1.3 on 2024-11-13 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_items_expiry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="expiry",
            field=models.DateField(default=datetime.date.today),
        ),
    ]