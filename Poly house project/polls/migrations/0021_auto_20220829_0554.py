# Generated by Django 3.2.15 on 2022-08-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20220827_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Password',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='address',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='c_pass',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='district',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='state',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='village',
            field=models.CharField(max_length=22),
        ),
    ]