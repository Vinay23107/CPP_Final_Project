# Generated by Django 4.0.2 on 2022-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='abc', upload_to='service'),
        ),
    ]