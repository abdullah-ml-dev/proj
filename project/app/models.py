from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    location = models.CharField(max_length=10)
    priority = models.CharField(max_length=10, default='normal')
    newsletter = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name