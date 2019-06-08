from django.shortcuts import render
from .models import UserInfo, AuthToken
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import UserInfoSerializers
from .utils import get_random_token

# Create your views here.


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializers


class UserNameDupChkAPIView(views.APIView):

    def post(self, request):
        res = {"status": 0, "Message": "OK"}
        user = UserInfo.objects.filter(user_name=request.data.get('user_name'))
        print(len(user))
        if len(user):
            res = {"status": 1, "Message": "Duplicate"}
        return Response(res)


class LoginAPIView(views.APIView):

    def post(self, request):
        res = {"status": 0, "Message": "OK", "AdminFlag": 0}
        user = UserInfo.objects.filter(user_name=request.data.get(
            'user_name'), password=request.data.get('password'))
        if not len(user):
            res = {"status": 1, "Message": "用户名或者密码错误"}
            return Response(res)

        cur_user = user.first()
        token = get_random_token(cur_user.user_name)
        AuthToken.objects.update_or_create(
            defaults={"token_code": token}, user_id=cur_user)
        res = {"status": 0, "Message": "OK",
               "AdminFlag": cur_user.user_type,
               "Token": token}
        return Response(res)
