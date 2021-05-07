# Generated by Django 3.1.7 on 2021-04-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20210418_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=53)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='hello.Flight')),
            ],
        ),
    ]