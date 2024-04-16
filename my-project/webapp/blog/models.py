from django.db import models

# Create your models here.
class MyBlogs(models.Model):
    titles = models.CharField(max_length=100)
    content = models.TextField
    date_posted = models.DateTimeField(auto_now_add=True)
    taa = models.CharField(max_length=100)
    image = models.TextField()
    views = models.IntegerField(default=10)
