# Generated by Django 3.2.9 on 2021-11-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunauteModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('dateCreation', models.DateField()),
                ('type', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]