# Generated by Django 4.1.4 on 2022-12-13 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('language', models.CharField(max_length=60)),
                ('picture', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file', models.BinaryField()),
                ('title', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('genere', models.CharField(max_length=60)),
                ('rating', models.IntegerField()),
                ('cahnnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.channel')),
            ],
        ),
    ]
