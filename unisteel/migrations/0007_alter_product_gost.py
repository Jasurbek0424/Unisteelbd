# Generated by Django 5.0.1 on 2024-02-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unisteel', '0006_alter_companiyinfo_options_alter_contacts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gost',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
