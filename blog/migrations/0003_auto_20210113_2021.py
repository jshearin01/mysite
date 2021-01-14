# Generated by Django 3.1.3 on 2021-01-14 01:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(null=True, upload_to='files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='intro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='powerpoint',
            field=models.FileField(null=True, upload_to='files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.ppt', '.pptx'])]),
        ),
    ]
