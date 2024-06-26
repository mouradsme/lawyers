# Generated by Django 4.2.7 on 2024-05-16 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_notary_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='rdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('remarques', models.CharField(max_length=1000)),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.lawyer')),
            ],
        ),
        migrations.CreateModel(
            name='nrdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('remarques', models.CharField(max_length=1000)),
                ('notary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.notary')),
            ],
        ),
        migrations.CreateModel(
            name='notaryclients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=60)),
                ('Sname', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('numcarte', models.IntegerField()),
                ('datecarte', models.DateField()),
                ('notary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.notary')),
            ],
        ),
        migrations.CreateModel(
            name='lawyerclients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=60)),
                ('Sname', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('numcarte', models.IntegerField()),
                ('datecarte', models.DateField()),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.lawyer')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
                ('aff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.aff')),
            ],
        ),
    ]
