from rest_framework import serializers
from .models import UserInfo, AuthToken


class UserInfoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        field = {'user_id', 'user_name', 'user_type', 'user_tel'}
