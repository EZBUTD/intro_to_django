from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    Identifier=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    comments=models.CharField(max_length=50)
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Identifier:{},Name:{}, ID: {}, Comment:{}>'.format(self.Identifier, self.name, self.id, self.comments)
