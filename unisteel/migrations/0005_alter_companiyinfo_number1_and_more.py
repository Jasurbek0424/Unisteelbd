# Generated by Django 5.0.1 on 2024-02-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unisteel', '0004_companiyinfo_servises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companiyinfo',
            name='number1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companiyinfo',
            name='number2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companiyinfo',
            name='number3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='servises',
            name='infoPreTitle',
            field=models.TextField(blank=True, null=True),
        ),
    ]
