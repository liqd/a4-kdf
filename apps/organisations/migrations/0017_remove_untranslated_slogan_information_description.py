# Generated by Django 2.2.16 on 2020-10-07 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_organisations', '0016_organisation_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='description_untranslated',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='information_untranslated',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='slogan_untranslated',
        ),
    ]
