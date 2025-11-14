from rest_framework import serializers


class CredentialsSerializer(serializers.Serializer):
    user = serializers.CharField()