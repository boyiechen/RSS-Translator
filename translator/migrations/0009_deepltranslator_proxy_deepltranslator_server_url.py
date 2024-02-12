# Generated by Django 5.0.1 on 2024-02-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('translator', '0008_geminitranslator'),
    ]

    operations = [
        migrations.AddField(
            model_name='deepltranslator',
            name='proxy',
            field=models.URLField(blank=True, null=True, verbose_name='Proxy(optional)'),
        ),
        migrations.AddField(
            model_name='deepltranslator',
            name='server_url',
            field=models.URLField(blank=True, null=True, verbose_name='API URL(optional)'),
        ),
    ]