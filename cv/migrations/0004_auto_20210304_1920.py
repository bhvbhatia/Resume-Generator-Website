# Generated by Django 3.0.3 on 2021-03-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20210303_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.TextField(),
        ),
    ]
