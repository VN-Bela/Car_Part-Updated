# Generated by Django 3.2.5 on 2021-08-17 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_name', models.CharField(max_length=100, null=True)),
                ('Car_model', models.CharField(max_length=100, null=True)),
                ('Car_Part_Name', models.CharField(max_length=100, null=True)),
                ('Car_Part_Info', models.CharField(choices=[('New', 'New'), ('Use', 'Use')], max_length=50)),
                ('Car_Part_Discription', models.CharField(max_length=100, null=True)),
                ('Owner_info', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Car_Part_App.category')),
            ],
        ),
    ]
