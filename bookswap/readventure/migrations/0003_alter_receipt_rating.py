# Generated by Django 4.2.7 on 2023-12-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readventure', '0002_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]