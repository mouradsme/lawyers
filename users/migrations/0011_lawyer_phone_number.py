# Generated by Django 4.2.7 on 2024-05-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_lawyerclient_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
