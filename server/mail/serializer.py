from rest_framework import serializers

from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class FormContactSerializer(serializers.Serializer):
    name = serializers.CharField()   
    email = serializers.EmailField()
    message = serializers.CharField()