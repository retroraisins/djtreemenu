# Generated by Django 2.0.1 on 2018-02-05 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='anonymous_only',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='login_required',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='treemenu.MenuItem'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
