# Generated by Django 3.1.3 on 2021-01-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(default='', max_length=70)),
                ('umur', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]