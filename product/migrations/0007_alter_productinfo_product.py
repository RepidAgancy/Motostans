# Generated by Django 4.2 on 2025-02-26 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_infoname_tech_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='product.product'),
        ),
    ]
