# Generated by Django 4.0.2 on 2022-03-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentasxpagarapp', '0007_alter_entradadocumento_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
    ]
