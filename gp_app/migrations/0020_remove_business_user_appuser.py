# Generated by Django 4.2.7 on 2023-11-26 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gp_app', '0019_business_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_biz', models.BooleanField(blank=True, default=False, verbose_name='Business')),
                ('city', models.CharField(choices=[('Colorado Springs', 'Colorado Springs'), ('Denver', 'Denver'), ('Fort Collins', 'Fort Collins')], default=None, max_length=200, verbose_name='Location')),
                ('business', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='gp_app.business', verbose_name='Favorite Business')),
                ('team', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='gp_app.nhlteam', verbose_name='Favorite Team')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
