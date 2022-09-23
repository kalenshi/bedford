from django.db import models


class Site(models.Model):
    description = models.CharField(max_length=255)
    active = models.BooleanField(blank=True)

    class Meta:
        managed = False
        app_label = "core"
        db_table = "site"
