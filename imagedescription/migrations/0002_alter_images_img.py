# Generated by Django 3.2.8 on 2021-10-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagedescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Imagen'),
        ),
    ]
