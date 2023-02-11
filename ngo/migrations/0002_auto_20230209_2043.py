# Generated by Django 2.2.24 on 2023-02-09 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ngouser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='ngos',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ngos',
            name='password',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='ngos',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
    ]