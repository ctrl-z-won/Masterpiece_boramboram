# Generated by Django 2.2.6 on 2019-10-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ill', 'illustration'), ('cha', 'character'), ('por', 'portrait'), ('cal', 'calligraphy'), ('web', 'webtoon'), ('vid', 'video'), ('oth', 'other')], max_length=3)),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('who_make', models.CharField(max_length=30)),
            ],
        ),
    ]
