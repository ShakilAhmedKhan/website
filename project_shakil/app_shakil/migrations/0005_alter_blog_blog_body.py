# Generated by Django 3.2.5 on 2021-07-31 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shakil', '0004_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]