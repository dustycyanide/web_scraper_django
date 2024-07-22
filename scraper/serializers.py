from rest_framework import serializers
from .models import LinkSubmission, ScrapedData

class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = ['id', 'key', 'value']


class LinkSubmissionSerializer(serializers.ModelSerializer):
    scraped_data = ScrapedDataSerializer(many=True, read_only=True)

    class Meta:
        model = LinkSubmission
        fields = ['id', 'link', 'created_at', 'updated_at', 'scraped_data']