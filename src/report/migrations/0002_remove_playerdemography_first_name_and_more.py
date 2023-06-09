# Generated by Django 4.2 on 2023-05-29 09:55

from django.db import migrations, models
import report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerdemography',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='playerdemography',
            name='last_name',
        ),
        migrations.AddField(
            model_name='playerdemography',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.CharField(default=report.models.Entry.generate_id, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
