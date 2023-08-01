from django.db import models

# Create your models here.
class Hotels(models.Model):
    image = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    des = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Booking(models.Model):
    cusname = models.CharField(max_length=50)
    hotlname = models.CharField(max_length=50)
    number = models.CharField(max_length=50, null=True)
    date = models.DateField()

class Comment(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    