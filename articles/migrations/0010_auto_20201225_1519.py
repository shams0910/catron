# Generated by Django 3.0.3 on 2020-12-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201225_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='articles.Category'),
        ),
    ]
