# Generated by Django 2.1.5 on 2022-01-17 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('secondname', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('Primaryscool', models.CharField(max_length=200)),
                ('highschool', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('position', models.CharField(default='Member', max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank='True', default='herbal.jpeg', upload_to='profilepics')),
                ('DateJoined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='herbal4.jpeg', upload_to='profilepics')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('projectname', models.CharField(max_length=200)),
                ('projectdescription', models.TextField()),
                ('projectmanager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
    ]
