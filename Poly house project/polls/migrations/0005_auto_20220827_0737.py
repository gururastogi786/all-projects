# Generated by Django 3.2.15 on 2022-08-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_contactus_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='number',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
    ]
