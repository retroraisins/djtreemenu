# Generated by Django 2.0.1 on 2018-02-05 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0015_auto_20180205_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='root_menu_item',
        ),
    ]
