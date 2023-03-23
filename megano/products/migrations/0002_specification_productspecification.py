# Generated by Django 4.1.7 on 2023-03-23 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='название')),
                ('category', models.ManyToManyField(related_name='specifications', to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'характеристика',
                'verbose_name_plural': 'характеристики',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=256, verbose_name='значение')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specification_name', to='products.specification', verbose_name='название')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specifications', to='products.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'характеристика продукта',
                'verbose_name_plural': 'характеристики продуктов',
            },
        ),
    ]
