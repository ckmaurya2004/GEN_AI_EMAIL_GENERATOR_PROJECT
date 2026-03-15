from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class GeneratedEmail(models.Model):

    user = models.CharField(max_length=100)
    email_type = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    purpose = models.TextField()
    generated_email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user