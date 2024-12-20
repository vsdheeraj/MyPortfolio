# Generated by Django 4.2.16 on 2024-11-23 20:41

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("headline", models.CharField(max_length=200)),
                (
                    "sub_headline",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default="/images/placeholder.png",
                        null=True,
                        upload_to="images",
                    ),
                ),
                ("body", django_ckeditor_5.fields.CKEditor5Field()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=False)),
                ("featured", models.BooleanField(default=False)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("tags", models.ManyToManyField(blank=True, to="base.tag")),
            ],
        ),
    ]
