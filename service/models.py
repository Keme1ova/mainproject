from django.db import models

class Offer(models.Model):
    img = models.ImageField(upload_to="")
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=True)
    text = models.TextField()

    def __str__(self):
        return self.title

