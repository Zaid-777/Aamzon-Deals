from django.db import models

# Create your models here.
class Products(models.Model):
    dealTitle = models.TextField()
    dealInfo = models.TextField()
    price = models.TextField()
    store = models.TextField()
    ratingNum = models.TextField()
    activityCol = models.TextField()
    lastPostCol = models.TextField()
    dealImg = models.TextField()
    dealLink = models.TextField()
    dealPostLink = models.TextField()

