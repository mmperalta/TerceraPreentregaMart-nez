# Generated by Django 5.0.6 on 2024-07-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ['-fechaEntrega']},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
