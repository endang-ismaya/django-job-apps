from django.db import models


class Upload(models.Model):
    image_url = models.ImageField(upload_to="images")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
