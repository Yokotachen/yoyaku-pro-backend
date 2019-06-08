from rest_framework import serializers
from .models import UserInfo, AuthToken


class UserInfoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_id', 'user_name', 'password', 'user_tel')
