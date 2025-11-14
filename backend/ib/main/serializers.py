from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import Organization, User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_staff','is_active','is_superuser','last_login','organization']

class UserMeSerializer(UserSerializer):
    class Meta:
        model = User
        read_only_fields = ['username','first_name','last_name','email','is_staff','is_active','is_superuser','last_login','organization']
        fields = ['username','first_name','last_name','email','is_staff','is_active','is_superuser','last_login','organization']
