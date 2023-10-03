# Generated by Django 4.2.5 on 2023-09-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='evidencia_img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='evidencia_img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('materias_imparte', models.ManyToManyField(related_name='maestro', to='app_crud_app.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='evidencia_img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('materias_cursa', models.ManyToManyField(related_name='alumnos', to='app_crud_app.materia')),
            ],
        ),
    ]
