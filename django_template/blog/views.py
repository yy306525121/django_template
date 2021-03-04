from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from django_template.common.rest_utils import Rsp


# Create your views here.

def index(request):
    return render(request=request, template_name='blog/index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    # raise Exception('1aaa')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST'])
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    serializer = UserSerializer(users, many=True)
    return Rsp.success(data=serializer.data)
    # return Rsp.fail(msg='查询错误')




