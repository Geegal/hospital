# Generated by Django 5.0.2 on 2024-02-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0007_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='fullname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='department',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]