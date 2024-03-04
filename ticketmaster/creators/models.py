from django.db import models

"""
Defines the model for the events creators
"""


class Creators(models.Model):
    """
    the creator class
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    password = models.CharField()
