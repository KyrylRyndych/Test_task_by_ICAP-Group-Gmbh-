# Generated by Django 4.2.5 on 2023-10-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='description',
            new_name='description1',
        ),
        migrations.AddField(
            model_name='goods',
            name='description2',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
