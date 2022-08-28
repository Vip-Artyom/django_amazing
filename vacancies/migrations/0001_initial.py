# Generated by Django 4.1 on 2022-08-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.CharField(max_length=50)),
                ("text", models.CharField(max_length=2000)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Черновик"),
                            ("open", "Открыта"),
                            ("closed", "Закрыта"),
                        ],
                        default="draft",
                        max_length=6,
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
