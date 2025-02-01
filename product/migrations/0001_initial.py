# Generated by Django 4.2 on 2025-02-01 16:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rgba_name', models.CharField(blank=True, max_length=250, null=True)),
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
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
            options={
                'verbose_name': 'main category',
                'verbose_name_plural': 'main categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity_left', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('price_type', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('item', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/images/')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
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
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
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
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='product.maincategory')),
            ],
            options={
                'verbose_name': 'sub category',
                'verbose_name_plural': 'sub categories',
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
            model_name='productcategory',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_categories', to='product.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_sub_categories', to='product.category'),
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
            model_name='product',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.maincategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.subcategory'),
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
                ('image_ru', models.ImageField(upload_to='discounted-product/image_ru')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounted_products', to='product.product')),
            ],
            options={
                'verbose_name': 'discounted product',
                'verbose_name_plural': 'discounted products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='product.productcategory'),
        ),
    ]
