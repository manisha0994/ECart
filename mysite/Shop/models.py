from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField()