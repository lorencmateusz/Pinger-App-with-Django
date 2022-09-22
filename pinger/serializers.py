from rest_framework import serializers

from pinger import models


class PingerSerializer(serializers.Serializer):
    hostname = serializers.CharField(max_length=10)
    connected = serializers.BooleanField(default=False)
    avg_time = serializers.CharField(max_length=3)
    date = serializers.DateTimeField()


class PingerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ping
        fields = ('hostname', 'connected', 'avg_time', 'date')
        extra_kwargs = {

        }

    def create(self, validated_data):
        ping = models.Ping.objects.create(
            hostname=validated_data['hostname'],
            connected=validated_data['connected'],
            avg_time=validated_data['avg_time'],
            date=validated_data['date']
        )

        return ping