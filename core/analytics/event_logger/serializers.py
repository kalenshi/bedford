from rest_framework import serializers

from models.analytics.event_logger import EventLoggerAnalytics


class EventLoggerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the EventLoggerDevelopment model in analytics schema
    """

    class Meta:
        model = EventLoggerAnalytics
        fields = (
            "id",
            "event",
            "created_at",
            "processed"
        )
