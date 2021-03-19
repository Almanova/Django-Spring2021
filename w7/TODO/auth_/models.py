from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name='User')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email address')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Last name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
