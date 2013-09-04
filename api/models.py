from django.db import models

# Create your models here.
class Trade(models.Model):
    time = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    type = models.CharField(max_length=4)
    
class Ticker(models.Model):
    last = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    vol = models.DecimalField(max_digits=10, decimal_places=2)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=30)
    coin = models.CharField(max_length=4)
    content = models.CharField(max_length=64)
    
class Depth(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    type = models.CharField(max_length=4)
    
class Alert(models.Model):
    #threshold = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)   
    
