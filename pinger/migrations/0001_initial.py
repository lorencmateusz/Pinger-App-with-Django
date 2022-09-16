# Generated by Django 4.1.1 on 2022-09-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=10)),
                ('connected', models.BooleanField(default=False)),
                ('avg_time', models.CharField(max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
