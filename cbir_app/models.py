from django.db import models


class Product(models.Model):
    image_id = models.CharField(max_length=100)
    feature_vector = models.JSONField(null=True)

