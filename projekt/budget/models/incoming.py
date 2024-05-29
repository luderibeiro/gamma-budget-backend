import uuid

from django.db import models


class Incoming(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    launch_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("IncomingCategory", on_delete=models.CASCADE, related_name="incoming")

    def __str__(self):
        return self.name
