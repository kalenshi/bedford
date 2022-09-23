from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.seo.member.serializers import MemberSerializer
from models.seo.member import Member


class MemberListView(APIView):
    """
    Class for interacting with the member model for CRUD operations
    """

    serializer_class = MemberSerializer

    def get(self, request, format=None):
        """
        List members  with any additional filtering provided
        """
        members = Member.objects.all()
        serializer = self.serializer_class(instance=members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                "location": openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
                "start_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description="The start date of the membership"
                ),
                "end_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description="The membership Termination date"
                ),

            },
            required=["name", "location", "start_date"]
        )
    )
    def post(self, request, format=None):
        """
        Provide functionality for adding members to the database
        - Note: as is, this will fail because the current postgres user
        - Does not have the necessary create privileges to post
        """
        return Response({"message": "Coming soon!"}, status=status.HTTP_201_CREATED)
