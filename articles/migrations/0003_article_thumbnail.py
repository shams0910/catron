# Generated by Django 3.0.3 on 2020-10-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201004_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
