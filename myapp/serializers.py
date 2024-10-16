from rest_framework import serializers
from .models import UserProfile, RoleProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email']
        
class RoleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleProfile
        fields = ['id', 'name']

