# Generated by Django 3.1.7 on 2021-05-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
