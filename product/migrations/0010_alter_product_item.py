# Generated by Django 4.2 on 2025-03-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_productinfo_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
