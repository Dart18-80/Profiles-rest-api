from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


"Controlador de Perfiles para los usuarios"
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=none):
        if not email:
            raise ValueError('Se debe agregar el Correo Electronico')

        email = self.normalize_email(email)
        user = self.model(email= email, name= name)
        user.set_password(password)
        user.save(using= self._db)

        return user

    "Guardar y crear un super Usuario"
    def create_superuser(self, email, name, password):
        user = self.create_use(email,name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
"""Modelo base de datos para los usuarios """
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfilesManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']


    "Funcion de Retorno de nombre completo"
    def get_full_name(self):
        return self.name

    "Funcion de Retorno de nombre pequeño"
    def get_short_name(self):
        return self.name

    "Funcion de Retorno de Email"
    def _str_(self):
        return self.email
