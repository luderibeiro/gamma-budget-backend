import uuid

from django.db import models


class IncomingCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class RevenueCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
