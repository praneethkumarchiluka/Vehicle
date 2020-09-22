from django.db import models

# Create your models here.
class items(models.Model):
    itemname=models.CharField(max_length=200)
    hsn=models.CharField(max_length=200)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    price=models.IntegerField()