from django.db import models
from askcompany.utils import uuid_upload_to

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField(upload_to=uuid_upload_to)
    photo=models.ImageField(blank=True)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<{self.pk}> {self.name}'