# Generated by Django 3.1.7 on 2021-03-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210328_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpus',
            name='updated_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='corpus',
            name='uploaded_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
