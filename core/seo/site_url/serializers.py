from rest_framework import serializers

from models.seo.site_url import SiteUrl


class SiteUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUrl
        fields = (
            "id",
            "url",
            "site"
        )
