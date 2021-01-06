# Generated by Django 3.1.3 on 2021-01-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.CharField(choices=[('PUB', 'Publish'), ('DRA', 'Save as Draft')], default='DRA', max_length=3),
        ),
    ]