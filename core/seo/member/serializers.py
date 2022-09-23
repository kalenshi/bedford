from rest_framework import serializers

from models.seo.member import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer class for the member model
    """

    class Meta:
        model = Member
        fields = (
            "id",
            "name",
            "location",
            "start_date",
            "end_date"
        )
