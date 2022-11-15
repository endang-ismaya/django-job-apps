from django.db import models
from django.utils.text import slugify
from enum import Enum


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}__{self.company}"


class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"


class JOB_TYPE(Enum):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        (JOB_TYPE.FULL_TIME.value, JOB_TYPE.FULL_TIME.value),
        (JOB_TYPE.PART_TIME.value, JOB_TYPE.PART_TIME.value),
    ]

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)
    job_type = models.CharField(
        max_length=200,
        null=False,
        choices=JOB_TYPE_CHOICES,
        default=JOB_TYPE.FULL_TIME.value,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"({self.id}) {self.title}"
