# Generated by Django 5.1.4 on 2025-01-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMusic', '0009_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
