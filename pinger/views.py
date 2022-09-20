from pinger import pinger_helper
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
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