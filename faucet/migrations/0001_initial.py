# Generated by Django 2.0.6 on 2018-06-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestNEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=80)),
                ('NEO', models.IntegerField()),
                ('GAS', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]