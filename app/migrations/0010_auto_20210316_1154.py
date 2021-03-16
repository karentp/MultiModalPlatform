# Generated by Django 3.1.7 on 2021-03-16 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210316_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segmentation',
            name='corpus_description',
        ),
        migrations.RemoveField(
            model_name='segmentation',
            name='corpus_name',
        ),
        migrations.RemoveField(
            model_name='segmentation',
            name='final_date_publication',
        ),
        migrations.RemoveField(
            model_name='segmentation',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='segmentation',
            name='recollection_country',
        ),
        migrations.RemoveField(
            model_name='segmentation',
            name='start_date_publication',
        ),
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpus_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recollection_country', models.CharField(blank=True, max_length=4, null=True)),
                ('corpus_description', models.CharField(blank=True, max_length=500, null=True)),
                ('start_date_publication', models.DateTimeField(blank=True, null=True)),
                ('final_date_publication', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Libro', 'Libro'), ('Revista', 'Revista'), ('Meme', 'Meme'), ('Publicidad', 'Publicidad')], max_length=40, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('segmentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.segmentation')),
            ],
        ),
    ]
