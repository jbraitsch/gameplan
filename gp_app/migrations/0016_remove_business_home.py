# Generated by Django 4.2.7 on 2023-11-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gp_app', '0015_business_home_alter_user_fav_biz_alter_user_fav_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='home',
        ),
    ]
