# Generated by Django 5.1.2 on 2024-12-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolioApp", "0003_post_delete_churchlike"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.IntegerField(default=116),
        ),
    ]