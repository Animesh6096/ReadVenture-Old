# Generated by Django 4.2.7 on 2023-11-30 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readventure', '0007_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='books',
            name='conditon',
        ),
        migrations.RemoveField(
            model_name='books',
            name='owner_id',
        ),
    ]