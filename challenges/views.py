from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from rest_framework import permissions
from challenges.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

challenge_list = {
    '1': 'do this',
    '2': 'do that',
    '3': 'do anything'

}


def index(request):
    return HttpResponse('all cool')


def monthly_challenges(request, month):
    return HttpResponse(f'its {month}')


# class PingerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Pinger.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]