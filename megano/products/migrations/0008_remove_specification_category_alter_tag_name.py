# Generated by Django 4.1.7 on 2023-03-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_title_specification_name_remove_product_href_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='category',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_index=True, default='', max_length=128, verbose_name='имя'),
        ),
    ]