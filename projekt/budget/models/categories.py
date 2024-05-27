from django.db import models


class IncomingCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class RevenueCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
