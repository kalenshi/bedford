from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.seo.site_url.serializers import SiteUrlSerializer
from models.seo.site_url import SiteUrl


class SiteUrlDetailView(APIView):
    """
    Class responsible for siteUrl CRUD operations
    """
    serializer_class = SiteUrlSerializer

    def get_object(self, url_id):
        """
        Retrieve a specific site_url by id

        Args:
            url_id (int) : The site primary key/id
        Returns:
            SiteUrl(object) : The site model
        """
        return get_object_or_404(SiteUrl, pk=url_id)

    def get(self, request, url_id, format=None):
        """
        Retrieve a list of siteUrls

        Args:
            request (object): The python request object
            url_id (int) : The primary key of the specific site_url
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        site_url = self.get_object(url_id)
        serializer = self.serializer_class(instance=site_url)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, url_id):
        """
        Provide functionality for `soft` deleting a site
        Args:
            url_id (int): the primary key of the site to delete
        Returns:
            Site (object): the site that has been deleted

        """

        site_url = self.get_object(url_id)
        site_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
