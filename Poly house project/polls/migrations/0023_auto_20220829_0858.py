# Generated by Django 3.2.15 on 2022-08-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20220829_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='age',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.AddField(
            model_name='contactus',
            name='Password',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AddField(
            model_name='contactus',
            name='address',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AddField(
            model_name='contactus',
            name='c_pass',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AddField(
            model_name='contactus',
            name='district',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AddField(
            model_name='contactus',
            name='state',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AddField(
            model_name='contactus',
            name='village',
            field=models.CharField(default=None, max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(default=None, max_length=22),
        ),
    ]
