# Generated by Django 4.1.3 on 2022-11-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_one", "0002_jobpost_date_jobpost_description_jobpost_salary"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(null=True),
        ),
    ]