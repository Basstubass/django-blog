# Generated by Django 3.2.6 on 2021-08-20 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contaent',
            new_name='content',
        ),
    ]
