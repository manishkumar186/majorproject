# Generated by Django 3.0.6 on 2020-12-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=200)),
                ('roll_no', models.IntegerField(unique=True)),
                ('fee', models.FloatField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=150)),
                ('address', models.TextField()),
                ('is_registered', models.BooleanField()),
            ],
        ),
    ]
