# Generated by Django 4.2.7 on 2024-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_subscriptionplan_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='notary',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
