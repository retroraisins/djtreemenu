# Generated by Django 2.0.1 on 2018-02-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0008_remove_menuitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link_url',
            field=models.CharField(max_length=100),
        ),
    ]