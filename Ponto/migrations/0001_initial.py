# Generated by Django 2.0.3 on 2018-04-01 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ponto', models.IntegerField(default=1)),
                ('nomePonto', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=700)),
                ('resumo', models.CharField(max_length=350)),
                ('distancia', models.FloatField()),
                ('duracao', models.FloatField()),
                ('desnivel', models.FloatField()),
                ('dificuldade', models.CharField(max_length=10)),
                ('coordenada_X', models.FloatField()),
                ('coordenada_Y', models.FloatField()),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Categoria.Categoria')),
            ],
        ),
    ]
