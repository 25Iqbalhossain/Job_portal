# Generated by Django 5.0.6 on 2024-05-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_candidatesingup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatesingup',
            old_name='fileinput',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='candidatesingup',
            name='address',
            field=models.TextField(max_length=122),
        ),
        migrations.AlterField(
            model_name='comsingup',
            name='address',
            field=models.TextField(max_length=122),
        ),
    ]