# Generated by Django 3.2.15 on 2022-11-28 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sacco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sacco_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=13)),
                ('invite_code', models.CharField(max_length=255)),
                ('sacco_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.sacco')),
            ],
        ),
    ]
