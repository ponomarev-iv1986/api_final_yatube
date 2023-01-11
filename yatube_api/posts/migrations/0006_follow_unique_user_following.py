# Generated by Django 3.2.16 on 2023-01-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_author_follow_following'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following'),
        ),
    ]