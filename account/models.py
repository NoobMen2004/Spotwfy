from django.db import models 
from django.contrib.auth.models import AbstractUser

import uuid
from django.conf import settings

from .manager import UserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=300, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        code = str(uuid.uuid4())
        self.activation_code = code

    def __str__(self):
        return f'{self.email}'
    
class UserActionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} - {self.action} at {self.timestamp}'