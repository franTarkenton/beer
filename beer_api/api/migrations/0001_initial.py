# Generated by Django 2.1.3 on 2018-12-01 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerList',
            fields=[
                ('beerId', models.AutoField(primary_key=True, serialize=False)),
                ('beerName', models.CharField(max_length=255, unique=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeerTypes',
            fields=[
                ('beerTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('beerType', models.CharField(max_length=255, unique=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beerTypes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='beerlist',
            name='beerType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beerTypeRel', to='api.BeerTypes'),
        ),
        migrations.AddField(
            model_name='beerlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beerlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
