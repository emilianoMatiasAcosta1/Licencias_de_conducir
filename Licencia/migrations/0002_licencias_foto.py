# Generated by Django 4.1.7 on 2023-05-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencias',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='mi_licencia'),
        ),
    ]