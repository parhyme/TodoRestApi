# Generated by Django 3.1 on 2020-08-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]