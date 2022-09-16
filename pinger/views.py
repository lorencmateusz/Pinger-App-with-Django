from pinger import pinger_helper
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from datetime import date

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

