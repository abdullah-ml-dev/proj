# Generated by Django 5.1.4 on 2024-12-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="msg",
            new_name="message",
        ),
        migrations.RenameField(
            model_name="contact",
            old_name="name",
            new_name="name1",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="date",
        ),
    ]