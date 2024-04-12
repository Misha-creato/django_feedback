from django.db import models


class Feedback(models.Model):
    title = models.CharField(
        max_length=128
    )
    text = models.TextField(
        max_length=256
    )
    full_name = models.CharField(
        max_length=128
    )
    contacts = models.CharField(
        max_length=64
    )

    def __str__(self):
        return f'{self.title}'
