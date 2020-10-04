# Generated by Django 2.1.15 on 2020-10-04 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_compra', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_total', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_marca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_lente', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='lente',
            name='idmarcas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lentes.Marca'),
        ),
        migrations.AddField(
            model_name='lente',
            name='idtipo_lente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lentes.TipoLente'),
        ),
        migrations.AddField(
            model_name='compra',
            name='idinventario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lentes.Lente'),
        ),
    ]