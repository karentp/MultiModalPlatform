# Generated by Django 3.1.7 on 2021-03-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210316_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='gender',
            field=models.CharField(blank=True, choices=[('Libro', 'Libro'), ('Revista', 'Revista'), ('Meme', 'Meme'), ('Publicidad', 'Publicidad')], max_length=40, null=True),
        ),
    ]
