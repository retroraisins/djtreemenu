# Generated by Django 2.0.1 on 2018-02-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0005_auto_20180205_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treemenu.MenuItem'),
        ),
    ]
