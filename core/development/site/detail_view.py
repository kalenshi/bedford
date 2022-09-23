from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.development.site.serializers import SiteSerializer
from models.development.site import Site


class SiteDetailView(APIView):
    """
    Class responsible for site CRUD operations
    """
    serializer_class = SiteSerializer

    def get_object(self, site_id):
        """
        Retrieve a specific site by id

        Args:
            site_id (int) : The site primary key/id
        Returns:
            Site(object) : The site model
        """
        return get_object_or_404(Site, pk=site_id)

    def get(self, request, site_id, format=None):
        """
        Retrieve a list of sites

        Args:
            request (object): The python request object
            site_id (int) : The primary key of the specific site
            format (str) :format string for accessing the results

        Returns:
            Response : python response object
        """
        site = self.get_object(site_id)
        serializer = self.serializer_class(instance=site)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, site_id):
        """
        Provide functionality for `soft` deleting a site
        Args:
            site_id (int): the primary key of the site to delete
        Returns:
            Site (object): the site that has been deleted

        """

        site = self.get_object(site_id)
        try:
            site.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return HttpResponseForbidden(f"{e}")
