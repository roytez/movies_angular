# Generated by Django 2.2.5 on 2020-05-21 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0013_auto_20200520_1722'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieHasDirector',
            new_name='MovieDirector',
        ),
        migrations.RenameModel(
            old_name='MovieHasGenre',
            new_name='MovieGenre',
        ),
        migrations.RemoveField(
            model_name='music',
            name='movie',
        ),
        migrations.AlterModelTable(
            name='moviedirector',
            table='movie_director',
        ),
        migrations.AlterModelTable(
            name='moviegenre',
            table='movie_genre',
        ),
    ]
