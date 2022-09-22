from pinger import pinger_helper, serializers, models
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, status, filters
import os
from datetime import date
from pinger.models import Ping

# Create your views here.


@api_view(http_method_names=['POST'])
def ping_ips(request):
    hostnames = request.data['hosts']
    print(hostnames)
    results = []
    try:
        for i in hostnames:
            cmd = os.popen(f"ping {i}").read()
            print(cmd)
            parsed_cmd_output = pinger_helper.output_parser(cmd)
            results.append(parsed_cmd_output)
            pinger_helper.save_results_to_db(parsed_cmd_output)
        print(results)
        return Response(results)
    except TypeError:
        return "make sure you used correct format - JSON {hosts: hostnames}"


class PingList(generics.ListAPIView):
    model = Ping

    def get_queryset(self):
        queryset = Ping.objects.all()
        host = self.request.query_params.get('host')

        if host:
            queryset = queryset.filter(hostname=host)
        return queryset


@api_view(http_method_names=['GET'])
def view_ping_history(request, queryset):

    pings = queryset
    return render(request, "history.html", {"pings": pings})

# viewsets, serializers


class HelloViewSet(viewsets.ViewSet):
    """Test api view"""
    queryset = Ping.objects.all()
    serializer_class = serializers.PingerSerializer
    hostname_separator = ','

    def get_queryset(self):
        hostnames = self.request.query_params.get('hostnames', None)
        if hostnames:
            qs = Ping.objects.filter()
            for hostname in hostnames.split(self.hostname_separator):
                qs = qs.filter(hostnames__name=hostname)

            return qs
    # def list(self, request):
    #     return Response({'message': 'Hello!', 'a_viewset': qs)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            hostname = serializer.validated_data.get('hostname')
            message = f'Added {hostname}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class PingerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PingerProfileSerializer
    queryset = models.Ping.objects.all()
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('hostname', 'date')



