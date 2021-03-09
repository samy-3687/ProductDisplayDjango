from django.db import models

class Productmodel(models.Model):
    prd_name = models.CharField(max_length = 50)
    prd_cat = models.CharField(max_length = 50)
    prd_price = models.IntegerField()
    prd_id = models.IntegerField()
    class Meta:
        db_table = 'Product_info'
