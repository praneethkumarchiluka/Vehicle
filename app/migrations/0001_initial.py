# Generated by Django 2.1.15 on 2020-08-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=20)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
