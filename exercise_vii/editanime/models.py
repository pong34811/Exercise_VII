from django.db import models

# Create your models here.
class Animal_list(models.Model):
    anime_order = models.IntegerField()
    anime_name_th = models.CharField(max_length=100)
    anime_name_en = models.CharField(max_length=100)
    anime_seasons = models.IntegerField()
    anime_channel = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)