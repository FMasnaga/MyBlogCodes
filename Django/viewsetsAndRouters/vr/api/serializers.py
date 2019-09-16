from rest_framework import serializers
from vr.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = "__all__"