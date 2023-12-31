# Generated by Django 4.2.7 on 2023-11-02 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gp_app', '0002_alter_business_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Colorado Springs', 'Colorado Springs'), ('Denver', 'Denver'), ('Fort Collins', 'Fort Collins')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='business',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gp_app.city'),
        ),
    ]
