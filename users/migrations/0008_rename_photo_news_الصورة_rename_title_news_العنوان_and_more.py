# Generated by Django 4.2.7 on 2024-05-03 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='photo',
            new_name='الصورة',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='العنوان',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='author',
            new_name='المؤلف',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='المحتوى',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='created_at',
            new_name='تاريخ_الإنشاء',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='updated_at',
            new_name='تاريخ_التحديث',
        ),
    ]
