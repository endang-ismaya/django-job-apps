# Generated by Django 4.1.3 on 2022-11-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_one", "0008_skill_jobpost_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="skills",
            field=models.ManyToManyField(to="app_one.skill"),
        ),
    ]
