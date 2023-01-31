from django.db import models


class Order(models.Model):
   name = models.CharField(max_length=255)
   fullname = models.CharField(max_length=255)
   number = models.IntegerField()
   typeofcar = models.TextField()
   nameofcar = models.TextField()
   data = models.DateTimeField()

   def __str__(self):
      return self.name
