from django.db import models

class Cards(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="") 
    type = models.TextField(null=True)

    def __str__(self):
        return self.name


class About_us(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Footer(models.Model):
    address = models.CharField(max_length=30)
    contacts = models.BigIntegerField()
    email = models.EmailField((""), max_length=254)


    def __str__(self):
        return self.address