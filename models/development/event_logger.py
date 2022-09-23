from django.db import models


class EventLoggerDevelopment(models.Model):
    event = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now=True)
    processed = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = '"development"."event_logger"'
        app_label = "core"
