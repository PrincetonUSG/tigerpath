# Generated by Django 4.1.2 on 2022-10-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigerpath', '0017_major_supported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='term_code',
            field=models.CharField(db_index=True, default=1232, max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_schedule',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_state',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
