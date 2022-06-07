from django.db import models

# Create your models here.
class options(models.Model):
    name = models.TextField(max_length=200)
    menu_items = models.CharField(max_length=200)
    reviews = models.IntegerField(default=0)
    


