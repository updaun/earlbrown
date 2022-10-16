from rest_framework import serializers
from .models import Menu, MenuImage


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuImageSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True)
    menu_id = serializers.CharField()

    class Meta:
        model = MenuImage
        fields = "__all__"
