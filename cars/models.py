from django.db import models

# Create your models here.
class Premium(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Jeep(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)




    def __str__(self):
        return self.name



class Limousine(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.name



class Cabriolets(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.name



class Retro(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.name



class Transfer(models.Model):
    img = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=25, null=True)
    seats = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.name



