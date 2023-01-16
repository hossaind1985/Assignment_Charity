from django.db import models


class charity(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    class Meta:
        db_table = 'Charity'
