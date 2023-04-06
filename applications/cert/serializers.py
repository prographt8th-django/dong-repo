from rest_framework import serializers

from applications.cert.models import University


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = "__all__"
