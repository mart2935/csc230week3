# Generated by Django 2.2.5 on 2019-09-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('adopted', models.BooleanField(default=False)),
            ],
        ),
    ]
