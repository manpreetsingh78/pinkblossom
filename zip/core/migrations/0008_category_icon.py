# Generated by Django 4.2.3 on 2023-07-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200510_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]