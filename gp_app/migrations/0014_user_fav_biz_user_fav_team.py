# Generated by Django 4.2.7 on 2023-11-22 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gp_app', '0013_user_remove_business_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_biz',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='gp_app.business'),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_team',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='gp_app.nhlteam'),
        ),
    ]
