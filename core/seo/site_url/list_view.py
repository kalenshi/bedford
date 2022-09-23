from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.seo.site_url.serializers import SiteUrlSerializer
from models.seo.site_url import SiteUrl


class SiteUrlListView(APIView):
    """
    Class responsible for site CRUD operations
    """
    serializer_class = SiteUrlSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="url",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="The url of the associated  site",
                required=False
            ),
            openapi.Parameter(
                name="site",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="The id os the associated site",
                required=False
            ),

        ]
    )
    def get(self, request, format=None):
        """
        Retrieve a list of sites_urls

        Args:
            request (object): The python request object
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        site_urls = SiteUrl.objects.all()
        serializer = self.serializer_class(instance=site_urls, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
