# Generated by Django 4.2.7 on 2024-05-08 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_message_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
    ]
