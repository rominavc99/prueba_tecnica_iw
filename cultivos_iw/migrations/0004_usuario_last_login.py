# Generated by Django 5.0.6 on 2024-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivos_iw', '0003_cultivo_illumination_cultivo_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]