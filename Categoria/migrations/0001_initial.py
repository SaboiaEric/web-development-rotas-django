# Generated by Django 2.0.3 on 2018-04-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categoria', models.IntegerField(default=1)),
                ('nomeCategoria', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=350)),
            ],
        ),
    ]
