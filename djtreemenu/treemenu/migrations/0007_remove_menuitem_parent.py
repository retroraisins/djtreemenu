# Generated by Django 2.0.1 on 2018-02-05 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0006_auto_20180205_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
    ]