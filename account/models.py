from django.db import models 
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=300, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        code = str(uuid.uuid4())
        self.create_activation_code

    def __str__(self):
        return self.email
    
