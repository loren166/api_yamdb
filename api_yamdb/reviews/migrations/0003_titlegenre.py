# Generated by Django 3.2 on 2023-02-09 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TitleGenre_genre', to='reviews.genre')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TitleGenre_title', to='reviews.title')),
            ],
        ),
    ]
