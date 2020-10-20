# Generated by Django 3.0.8 on 2020-10-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviews',
        ),
    ]