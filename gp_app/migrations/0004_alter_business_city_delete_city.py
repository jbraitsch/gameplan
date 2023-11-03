# Generated by Django 4.2.7 on 2023-11-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp_app', '0003_city_alter_business_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='city',
            field=models.CharField(choices=[('Colorado Springs', 'Colorado Springs'), ('Denver', 'Denver'), ('Fort Collins', 'Fort Collins')], max_length=200, verbose_name='Location'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]