# Generated by Django 3.2.1 on 2021-05-06 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_notification_rules_notifications'),
    ]

    operations = [
        migrations.DeleteModel(
            name='notification_rules',
        ),
        migrations.DeleteModel(
            name='notifications',
        ),
    ]