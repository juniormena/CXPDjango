# Generated by Django 4.0.2 on 2022-03-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentasxpagarapp', '0003_entradadocumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradadocumento',
            name='numeroDocumento',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='entradadocumento',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='entradadocumento',
            name='fechaDocumento',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entradadocumento',
            name='fechaRegistro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entradadocumento',
            name='numeroFactura',
            field=models.CharField(default='', max_length=12),
        ),
    ]