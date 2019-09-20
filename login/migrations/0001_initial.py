# Generated by Django 2.2.5 on 2019-09-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('user_nickname', models.CharField(max_length=200)),
            ],
        ),
    ]
