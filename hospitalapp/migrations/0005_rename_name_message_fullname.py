# Generated by Django 5.0.2 on 2024-02-28 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='fullname',
        ),
    ]
