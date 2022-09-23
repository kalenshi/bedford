from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.seo.member.serializers import MemberSerializer
from models.seo.member import Member


class MemberDetailView(APIView):
    """
    Class for interacting with the member model for CRUD operations
    Using and existing ID
    """

    serializer_class = MemberSerializer

    def get_object(self, mem_id):
        """
        Retrieve a specific member from the database
        Args:
            mem_id (int) : the primary key of the member to retrieve
        Returns:
            Member (object) : The member with the given member id
        """
        return get_object_or_404(Member, pk=mem_id)

    def get(self, request, mem_id, format=None):
        """
        List members  with any additional filtering provided
        """
        member = self.get_object(mem_id)
        serializer = self.serializer_class(instance=member)

        return Response(serializer.data, status=status.HTTP_200_OK)
