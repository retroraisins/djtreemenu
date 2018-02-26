# Generated by Django 2.0.1 on 2018-02-05 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0016_remove_menu_root_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treemenu.MenuItem'),
        ),
    ]