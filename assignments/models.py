from django.db import models


class Assignment(models.Model):
    candidate = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    email = models.CharField(max_length=300)
    dropbox_id = models.CharField(max_length=100)
    reviewed = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
