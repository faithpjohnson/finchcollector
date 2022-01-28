# Generated by Django 4.0.1 on 2022-01-27 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_finch_toys'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='finch',
            old_name='type',
            new_name='breed',
        ),
        migrations.AddField(
            model_name='feeding',
            name='finch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.finch'),
            preserve_default=False,
        ),
    ]