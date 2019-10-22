from django.db import models


# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=300)
    last_update = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField()


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, verbose_name="List")
    text = models.CharField(max_length=500, verbose_name="Text")
    checked = models.BooleanField(default=False, verbose_name="Checked")
    checked_date = models.DateTimeField(default=None, blank=True)
    creation_date = models.DateTimeField()
