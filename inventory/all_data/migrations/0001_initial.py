# Generated by Django 4.0.5 on 2022-06-17 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventary_number', models.IntegerField(max_length=12)),
                ('serial_number', models.IntegerField(max_length=24)),
                ('computer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_data.computer')),
            ],
        ),
    ]