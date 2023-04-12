from rest_framework import serializers

from applications.cert.models import University, User


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["password", "last_login"]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

