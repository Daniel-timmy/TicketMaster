from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
import uuid

"""
Defines the model for the events creators
"""


class Creator(models.Model):
    """
    the creator class
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    password = models.CharField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')
