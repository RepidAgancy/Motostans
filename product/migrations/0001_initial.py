# Generated by Django 4.2 on 2024-12-19 12:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rgba_name', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='InfoName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'info name',
                'verbose_name_plural': 'info names',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product/images/')),
                ('name', models.CharField(max_length=250)),
                ('name_uz', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('discount_percentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_discount', models.BooleanField(default=False)),
                ('is_top', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('name_uz', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'product brand',
                'verbose_name_plural': 'product brands',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('name_uz', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'product category',
                'verbose_name_plural': 'product categories',
            },
        ),
        migrations.CreateModel(
            name='TechnicalInfoName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_names', to='product.productcategory')),
            ],
            options={
                'verbose_name': 'technical information name',
                'verbose_name_plural': 'technical information names',
            },
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('media', models.ImageField(upload_to='product-media/medias/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='product.product')),
            ],
            options={
                'verbose_name': 'product media',
                'verbose_name_plural': 'product medias',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('info_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='product.infoname')),
                ('tech_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='product.technicalinfoname')),
            ],
            options={
                'verbose_name': 'product info',
                'verbose_name_plural': 'product infos',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.productbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.colors'),
        ),
        migrations.AddField(
            model_name='product',
            name='infos',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.productinfo'),
        ),
        migrations.AddField(
            model_name='infoname',
            name='tech_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_names', to='product.technicalinfoname'),
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_uz', models.ImageField(upload_to='discounted-product/image_uz')),
                ('image_ru', models.ImageField(upload_to='discounted-product/image_ru')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounted_products', to='product.product')),
            ],
            options={
                'verbose_name': 'discounted product',
                'verbose_name_plural': 'discounted products',
            },
        ),
    ]