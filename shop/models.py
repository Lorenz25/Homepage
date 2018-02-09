from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='items')
    description = models.TextField()

    def __str__(self):
        return self.title
