# Generated by Django 2.2.1 on 2019-06-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20190613_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
