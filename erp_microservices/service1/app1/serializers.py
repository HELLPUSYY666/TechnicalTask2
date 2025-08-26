from rest_framework import serializers

from .models import User


class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "created_at"]
