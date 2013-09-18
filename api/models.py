from django.db import models

# Create your models here.
class Trade(models.Model):
    time = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4)
    
    class Meta:
        abstract = True
    
class MtgoxTrade(Trade):
    pass
    class Meta(Trade.Meta):
        db_table = 'MtgoxTrade'
        
class Futures796Trade(Trade):
    pass
    class Meta(Trade.Meta):
        db_table = 'Futures796Trade'
        
class Stockpd796Trade(Trade):
    pass
    class Meta(Trade.Meta):
        db_table = 'Stockpd796Trade'   

    
class Ticker(models.Model):
    last = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    high = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    low = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    vol = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    sell = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    name = models.CharField(max_length=30)
    coin = models.CharField(max_length=4)
    content = models.CharField(max_length=64)
    ticker = models.CharField(max_length=64)#ticker API
    depth = models.CharField(max_length=64)#depth API
    trade = models.CharField(max_length=64)#trade API
    
class Depth(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    type = models.CharField(max_length=4)
    
class Alert(models.Model):
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2) 
    username = models.CharField(max_length=32)
    market = models.CharField(max_length=32)  
    
class Account(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    mail = models.CharField(max_length=32)
    QQ = models.CharField(max_length=32)
    baojing = models.CharField(max_length=32)
    baojingdown = models.CharField(max_length=32)
    qqbaojing = models.CharField(max_length=32)
    qqbaojingdown = models.CharField(max_length=32) 
    
