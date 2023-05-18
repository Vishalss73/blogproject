# Generated by Django 4.1.3 on 2022-12-13 22:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogpapp', '0003_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category_title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='sno',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='sno',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='sno',
            new_name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='post_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=False,
        ),
    ]