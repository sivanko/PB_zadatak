# Generated by Django 3.2.7 on 2022-03-09 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evidencijatroskova', '0002_alter_evidencija_ev_vrsta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidencija',
            name='ev_vrsta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidencija_id', to='evidencijatroskova.troskovi'),
        ),
    ]