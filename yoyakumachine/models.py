from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True, db_column="用户编号")
    user_name = models.EmailField(null=False, blank=False, unique=True, db_column="用户名")
    password = models.CharField(null=False, blank=False, max_length=128, db_column="密码")
    user_type = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        db_column="管理员"
    ) 
    user_tel = models.CharField(default='9352', null=False, blank=False, max_length=20, db_column="电话")
    user_createTime = models.DateField(auto_now_add=True, db_column="创建时间")
    user_updateTime = models.DateField(auto_now=True, db_column="更新时间")

    def __str__(self):
        return self.user_name

class AuthToken(models.Model):
    token_id = models.AutoField(primary_key=True, db_column="证书编号")
    user_id = models.OneToOneField(to='UserInfo', to_field='user_id', on_delete=models.CASCADE)
    token_code = models.CharField(max_length=128, db_column="证书")

    def __str__(self):
        return self.token_code