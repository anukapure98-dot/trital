from django.contrib import admin

# Register your models here.
from django.db import models

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    parent_mobile = models.CharField(max_length=15)
    special_work = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    