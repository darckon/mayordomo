from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)
    created_at = models.DateTimeField(("creado el"), auto_now_add=True)
    updated_at = models.DateTimeField(("actualizado el"), auto_now=True)
        
    class Meta:
        """ 
        User.
            username
            password
            first_name
            last_name
            email
            is_staff
            is_active
            date_joined
        """
        ordering = ('first_name', )
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")