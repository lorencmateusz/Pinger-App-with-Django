from rest_framework import serializers


class PingerSerializer(serializers.Serializer):
    hostname = serializers.CharField(max_length=10)
    connected = serializers.BooleanField(default=False)
    avg_time = serializers.CharField(max_length=3)
    date = serializers.DateTimeField()
