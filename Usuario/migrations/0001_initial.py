# Generated by Django 2.0.3 on 2018-03-31 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=100)),
                ('CPF', models.CharField(max_length=15)),
                ('local_x', models.CharField(max_length=100)),
                ('local_y', models.CharField(max_length=100)),
                ('id_usuario', models.IntegerField(default=1)),
            ],
        ),
    ]