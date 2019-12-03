from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)
    created_date = models.DateField(auto_now_add = True)
    modified_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.title