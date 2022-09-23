from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.analytics.event_logger.serializers import EventLoggerSerializer
from models.development.event_logger import EventLoggerDevelopment


class EventLoggerDevelopmentDetailView(APIView):
    """
    Class responsible for EventLoggerDevelopment CRUD operations
    """
    serializer_class = EventLoggerSerializer

    def get_object(self, event_id):
        """
        Retrieve the event logger details with the given id

        """
        return get_object_or_404(EventLoggerDevelopment, pk=event_id)

    def get(self, request, event_id, format=None):
        """
        Retrieve a list of Logged events

        Args:
            request (object): The python request object
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        event_logger = self.get_object(event_id)
        serializer = self.serializer_class(instance=event_logger)

        return Response(serializer.data, status=status.HTTP_200_OK)
