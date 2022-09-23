from rest_framework import serializers

from models.development.event_logger import EventLoggerDevelopment


class EventLoggerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the EventLoggerDevelopment model in analytics schema
    """

    class Meta:
        model = EventLoggerDevelopment
        fields = (
            "id",
            "event",
            "created_at",
            "processed"
        )
