# Generated by Django 3.0.6 on 2020-05-18 15:57

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('image', imagekit.models.fields.ProcessedImageField(default='ingredients/ingredient_default.jpg', upload_to='ingredients')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'ingredients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('image', imagekit.models.fields.ProcessedImageField(default='dishes/dish_default.jpg', upload_to='dishes')),
                ('description', models.TextField(blank=True)),
                ('recipe', models.TextField(blank=True)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
            options={
                'verbose_name_plural': 'dishes',
                'ordering': ['name'],
            },
        ),
    ]
