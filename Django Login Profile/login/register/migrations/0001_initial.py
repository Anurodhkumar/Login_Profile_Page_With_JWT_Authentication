# Generated by Django 3.1.4 on 2021-05-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=128)),
                ('lname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
    ]
