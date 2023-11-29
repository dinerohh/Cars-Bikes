from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
