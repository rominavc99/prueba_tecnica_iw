# Generated by Django 5.0.6 on 2024-05-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivos_iw', '0002_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivo',
            name='illumination',
            field=models.CharField(choices=[('Sol', 'Sol'), ('Media Sombra', 'Media Sombra'), ('Sombra', 'Sombra')], default='Sol', max_length=12),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='type',
            field=models.CharField(choices=[('Hortalizas', 'Hortalizas'), ('Flores', 'Flores'), ('Aromáticas', 'Aromáticas')], default='Hortalizas', max_length=10),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='season',
            field=models.CharField(choices=[('Primavera', 'Primavera'), ('Verano', 'Verano'), ('Otoño', 'Otoño'), ('Invierno', 'Invierno'), ('Cualquiera', 'Cualquiera')], default='Primavera', max_length=10),
        ),
    ]
