# Generated by Django 4.0.4 on 2022-05-29 21:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
