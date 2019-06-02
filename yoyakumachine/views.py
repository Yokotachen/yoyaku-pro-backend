from django.shortcuts import render
from .models import UserInfo
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import UserInfoSerializers

# Create your views here.


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializers


class UserInfoContrlAPIView(views.APIView):

    def post(self, request):
        res = {"status": 0, "Message": "OK"}
        print(request)
        return Response(res)
