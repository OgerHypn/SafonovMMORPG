# Generated by Django 4.1.6 on 2023-08-31 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appboard', '0003_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='status',
            field=models.CharField(choices=[('C', 'Создан'), ('A', 'Принят'), ('D', 'Отклонен')], default='C', max_length=1, verbose_name='Статус'),
        ),
    ]
