from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer


# Create your views here.

def index(request):
    return render(request=request, template_name='blog/index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
