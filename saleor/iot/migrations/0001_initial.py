# Generated by Django 2.2.6 on 2020-07-27 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('imageName', models.CharField(max_length=256)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]