# Generated by Django 4.1.3 on 2022-12-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
