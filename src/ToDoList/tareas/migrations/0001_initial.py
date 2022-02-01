# Generated by Django 4.0.1 on 2022-01-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
                ('comments', models.CharField(max_length=50, verbose_name='Comentarios')),
                ('status', models.CharField(choices=[('A', 'To Do'), ('B', 'In Progress'), ('C', 'Done'), ('D', 'Close')], default='A', max_length=4, verbose_name='Estado')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de vencimiento')),
            ],
        ),
    ]
