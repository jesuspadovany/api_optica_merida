# Generated by Django 2.1.15 on 2020-10-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lentes', '0002_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lente',
            old_name='idmarcas',
            new_name='marcas',
        ),
        migrations.RenameField(
            model_name='lente',
            old_name='idtipo_lente',
            new_name='tipo_lente',
        ),
        migrations.AlterField(
            model_name='lente',
            name='foto',
            field=models.ImageField(upload_to='lentes'),
        ),
    ]