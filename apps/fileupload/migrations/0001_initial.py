# Generated by Django 2.0.3 on 2018-03-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Archivos')),
                ('slug', models.SlugField(blank=True, max_length=100)),
            ],
        ),
    ]
