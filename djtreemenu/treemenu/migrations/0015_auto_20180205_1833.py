# Generated by Django 2.0.1 on 2018-02-05 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0014_auto_20180205_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='root_menu_item',
            new_name='root_menu',
        ),
    ]