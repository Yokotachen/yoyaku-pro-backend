# Generated by Django 2.2.1 on 2019-06-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyakumachine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(db_column='用户名', max_length=128, unique=True),
        ),
    ]
