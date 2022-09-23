from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.analytics.event_logger.serializers import EventLoggerSerializer
from models.development.event_logger import EventLoggerDevelopment


class EventLoggerDevelopmentListView(APIView):
    """
    Class responsible for EventLoggerDevelopment CRUD operations
    """
    serializer_class = EventLoggerSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="event",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="The url of the associated  site",
                required=False
            ),
            openapi.Parameter(
                name="processed",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                description="Processed or not ",
                required=False
            ),

        ]
    )
    def get(self, request, format=None):
        """
        Retrieve a list of Logged events

        Args:
            request (object): The python request object
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        event_loggers = EventLoggerDevelopment.objects.all()
        serializer = self.serializer_class(instance=event_loggers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
