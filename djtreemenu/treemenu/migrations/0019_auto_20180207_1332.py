# Generated by Django 2.0.1 on 2018-02-07 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0018_auto_20180206_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='root_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treemenu.Menu'),
        ),
    ]