# Generated by Django 4.2.10 on 2024-02-09 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vistas_Clases', '0003_remove_usuarios_last_login_remove_usuarios_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomtarea', models.CharField(max_length=25)),
                ('desctarea', models.CharField(max_length=150)),
                ('iniciftarea', models.DateField()),
                ('finftarea', models.DateField()),
                ('usuario_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vistas_Clases.usuarios')),
            ],
        ),
    ]
