# Generated by Django 2.2.17 on 2020-11-23 12:52

import adhocracy4.ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0005_module_is_draft'),
        ('a4_candy_questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStream',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a4modules.Item')),
                ('live_stream', adhocracy4.ckeditor.fields.RichTextCollapsibleUploadingField(blank=True, verbose_name='Live Stream')),
            ],
            options={
                'abstract': False,
            },
            bases=('a4modules.item',),
        ),
    ]