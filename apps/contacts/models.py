from django.db import models
from apps.users.models import CustomUser

 
class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.title}'