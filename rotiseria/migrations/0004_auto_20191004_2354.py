# Generated by Django 2.1.1 on 2019-10-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotiseria', '0003_auto_20191004_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
