# Generated by Django 3.2.8 on 2021-10-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
                ('adherent', models.IntegerField(null=True)),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('type_commu', models.CharField(choices=[('PV', 'Prive'), ('PU', 'Public'), ('RE', 'Restreint')], default='PU', max_length=2)),
            ],
        ),
    ]
