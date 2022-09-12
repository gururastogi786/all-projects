# Generated by Django 3.2.15 on 2022-09-05 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='')),
                ('dist_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.district')),
                ('state_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.state')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100)),
                ('sub_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_1.user')),
            ],
        ),
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('f_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_1.user')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state_dist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.state'),
        ),
    ]
