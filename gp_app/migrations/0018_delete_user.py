# Generated by Django 4.2.7 on 2023-11-25 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gp_app', '0017_rename_fav_biz_user_business_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
