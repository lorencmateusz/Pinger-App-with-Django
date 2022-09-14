from django.shortcuts import render
from django.http import HttpResponse, Http404

challenge_list = {
    '1': 'do this',
    '2': 'do that',
    '3': 'do anything'

}


def index(request):
    return HttpResponse('all cool')


def monthly_challenges(request, month):
    return HttpResponse(f'its {month}')

