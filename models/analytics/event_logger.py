from django.db import models


class EventLoggerAnalytics(models.Model):
    event = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now=True)
    processed = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = '"analytics"."event_logger"'
        app_label = "core"
