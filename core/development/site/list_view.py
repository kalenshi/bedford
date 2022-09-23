from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.development.site.serializers import SiteSerializer
from models.development.site import Site


class SiteListView(APIView):
    """
    Class responsible for site CRUD operations
    """
    serializer_class = SiteSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="description",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="The description of the intended site",
                required=False
            ),

        ]
    )
    def get(self, request, format=None):
        """
        Retrieve a list of sites

        Args:
            request (object): The python request object
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        sites = Site.objects.all()
        serializer = self.serializer_class(instance=sites, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
