# Generated by Django 5.0.1 on 2024-02-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("unisteel", "0005_alter_companiyinfo_number1_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="companiyinfo",
            options={"verbose_name": "Информация", "verbose_name_plural": "Информации"},
        ),
        migrations.AlterModelOptions(
            name="contacts",
            options={"verbose_name": "Контакт", "verbose_name_plural": "Контакты"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукты"},
        ),
        migrations.AlterModelOptions(
            name="rekviziti",
            options={"verbose_name": "Реквизит", "verbose_name_plural": "Реквизиты"},
        ),
        migrations.AlterModelOptions(
            name="servises",
            options={"verbose_name": "Сервис", "verbose_name_plural": "Сервисы"},
        ),
        migrations.AlterField(
            model_name="product",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
