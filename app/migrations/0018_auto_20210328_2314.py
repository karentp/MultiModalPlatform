# Generated by Django 3.1.7 on 2021-03-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_corpus_corpus_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='final_date_publication',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='start_date_publication',
            field=models.DateField(blank=True, null=True),
        ),
    ]
