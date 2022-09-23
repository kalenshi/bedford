from django.db import models

from models.development.site import Site


class SiteUrl(models.Model):
    url = models.CharField(max_length=255)
    site = models.ForeignKey(to=Site, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = "core"
        db_table = '"seo"."site_url"'
