# Generated by Django 2.1.15 on 2020-08-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_items_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='hsn',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]