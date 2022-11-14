from django.db import models
from enum import Enum


class NEWSLETTER(Enum):
    WEEKLY = "W"
    MONTHLY = "M"


NEWSLETTER_OPTION = [
    (NEWSLETTER.WEEKLY.value, "Weekly"),
    (NEWSLETTER.MONTHLY.value, "Monthly"),
]

# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(
        max_length=2, choices=NEWSLETTER_OPTION, default=NEWSLETTER.WEEKLY.value
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
