# Generated by Django 3.0.5 on 2020-05-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AudioShare', '0002_auto_20200513_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='original_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AudioShare.Post'),
        ),
    ]
