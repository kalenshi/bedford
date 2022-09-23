from django.db import models


class Team(models.Model):
    category_choices = [
        ("soccer", "SOCCER"),
        ("football", "FOOTBALL"),
        ('volleyball', "VOLLEYBALL"),
        ("basketball", "BASKETBALL"),
        ("hockey", "HOCKEY"),
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices, max_length=80)
    active = models.BooleanField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "core"
        db_table = '"analytics"."team"'
