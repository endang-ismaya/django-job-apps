# Generated by Django 4.1.3 on 2022-11-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_one", "0010_alter_skill_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="type",
            field=models.CharField(
                choices=[("Full Time", "Full Time"), ("Part Time", "Part Time")],
                default="Full Time",
                max_length=200,
            ),
        ),
    ]
