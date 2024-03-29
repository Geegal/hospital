# Generated by Django 5.0.2 on 2024-02-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0006_alter_message_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=30)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=300)),
                ('doctor', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
