# Generated by Django 4.0.4 on 2022-06-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mm_name', models.CharField(max_length=200, verbose_name='Название раздела')),
                ('mm_link', models.CharField(max_length=200, null=True, verbose_name='Алиас')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Главное Меню',
            },
        ),
    ]
