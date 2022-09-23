from rest_framework import serializers

from models.development.site import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            "id",
            "description",
            "active"
        )
