# Generated by Django 4.2.5 on 2023-10-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_goods_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='description1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='photo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
