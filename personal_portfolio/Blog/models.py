from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    date=models.DateField()
    def __str__(self):
        return self.title