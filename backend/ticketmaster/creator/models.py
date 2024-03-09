from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
import uuid

from django.utils import timezone

"""
Defines the custom model for the events creators(users)
"""


class CreatorProfileManager(BaseUserManager):
    """
    Defines Creators creation fields and manages to save user
    """

    def create(self, email, password, **extra_fields):
        """

        :param name:
        :param company_name:
        :param self:
        :param email:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('Email address required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
         Create and save a SuperUser with the given email and password.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create(email, password, **extra_fields)


class Creator(AbstractBaseUser, PermissionsMixin):
    """
    the creator class
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(unique=True)
    password = models.CharField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # reservations = GenericRelation(Reservation)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CreatorProfileManager()

    def __str__(self):
        return self.email
