# Generated by Django 4.1.3 on 2022-12-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
