# Generated by Django 2.1.7 on 2019-03-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputfile',
            name='ufile',
            field=models.FileField(null=True, upload_to='csv/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='inputfile',
            name='uname',
            field=models.CharField(max_length=200),
        ),
    ]
