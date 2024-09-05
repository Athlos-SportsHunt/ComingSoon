from django.db import models

# Create your models here.

class Updates(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f" mail:{self.email}"