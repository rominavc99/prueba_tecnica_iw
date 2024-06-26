# Generated by Django 5.0.6 on 2024-05-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivos_iw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
            ],
        ),
    ]
