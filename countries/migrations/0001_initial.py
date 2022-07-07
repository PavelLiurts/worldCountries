# Generated by Django 4.0.6 on 2022-07-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('capital', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
