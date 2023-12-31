# Generated by Django 4.2 on 2023-11-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
                ("published_at", models.DateField(blank=True, null=True)),
                ("author", models.TextField(blank=True, null=True)),
                ("publisher", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                ("keywords", models.TextField(blank=True, null=True)),
                ("header_image", models.TextField(blank=True, null=True)),
                ("raw_description", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("scraped_at", models.DateField(blank=True, null=True)),
                ("img_id", models.ImageField(upload_to="images/")),
            ],
            options={
                "db_table": "news",
                "managed": False,
            },
        ),
    ]
