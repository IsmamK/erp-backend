# Generated by Django 4.2.16 on 2024-11-05 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0014_alter_return_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="return",
            name="warehouse",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.warehouse",
            ),
        ),
    ]
