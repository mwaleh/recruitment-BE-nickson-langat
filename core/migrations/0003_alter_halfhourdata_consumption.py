# Generated by Django 3.2.8 on 2021-10-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_halfhourdata_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halfhourdata',
            name='consumption',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
