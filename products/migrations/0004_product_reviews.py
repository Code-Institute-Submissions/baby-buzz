# Generated by Django 3.0.8 on 2020-10-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201011_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.TextField(blank=True, default=False, null=True),
        ),
    ]
