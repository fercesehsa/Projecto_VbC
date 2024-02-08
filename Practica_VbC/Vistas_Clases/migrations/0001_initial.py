# Generated by Django 5.0.1 on 2024-02-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuaios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usenom', models.CharField(max_length=25)),
                ('appuse', models.CharField(max_length=25)),
                ('apmuse', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
