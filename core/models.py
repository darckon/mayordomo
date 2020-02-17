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


class Butler(models.Model):
    name = models.CharField('nombre', max_length=100)
    created_at = models.DateTimeField(("creado el"), auto_now_add=True)
    updated_at = models.DateTimeField(("actualizado el"), auto_now=True)

    class Meta:
        verbose_name = ("Mayordomo")
        verbose_name_plural = ("Mayordomos")

    def __str__(self):
        return '%s' % (self.name)

    
class Specialties(models.Model):
    name = models.CharField('nombre', max_length=100)
    created_at = models.DateTimeField(("creado el"), auto_now_add=True)
    updated_at = models.DateTimeField(("actualizado el"), auto_now=True)

    class Meta:
        verbose_name = ("Especialidad")
        verbose_name_plural = ("Especialidades")

    def __str__(self):
        return '%s' % (self.name)


class UserButlerSpecialty(models.Model):
    user = models.OneToOneField("core.User", db_index=True, related_name='user_butler_speciality_set', verbose_name=("usuario"), on_delete=models.CASCADE, unique=True)
    butler = models.OneToOneField("core.Butler", db_index=True, related_name='user_butler_speciality_set', verbose_name=("mayordomo"), on_delete=models.CASCADE, unique=True)
    speciality = models.ManyToManyField("core.Specialties", db_index=True, related_name='user_butler_speciality_set', verbose_name=("especialidad"))
    
    created_at = models.DateTimeField(("creado el"), auto_now_add=True)
    updated_at = models.DateTimeField(("actualizado el"), auto_now=True)

    class Meta:
        verbose_name = ("Usuario - Mayordomo - Especialidad")
        verbose_name_plural = ("Usuarios - Mayordomos - Especialidades")

    def __str__(self):
        return '%s :: %s :: %s' % (self.user, self.butler, self.speciality)