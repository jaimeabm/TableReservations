# Generated by Django 2.2.7 on 2019-11-15 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField()),
                ('persons', models.IntegerField()),
                ('message', models.TextField(blank=True)),
                ('guess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Guess')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Table')),
            ],
        ),
    ]