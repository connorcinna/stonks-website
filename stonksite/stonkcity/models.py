from django.db import models
from stonks import rt_stock_price

class Images(models.Model): 
    name = models.CharField(max_length=50) 
    image_Main_Img = models.ImageField(upload_to='images/') 
