from django.db import models
from django.utils import timezone

class Contact(models.Model):
    LOCATION_CHOICES = [
        ('home', 'Home'),
        ('office', 'Office'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='home')
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name