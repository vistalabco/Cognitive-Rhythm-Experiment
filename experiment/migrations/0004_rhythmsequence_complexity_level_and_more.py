# Generated by Django 5.1.2 on 2024-11-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiment", "0003_remove_trial_ear_first_order_trial_sequence_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="rhythmsequence",
            name="complexity_level",
            field=models.CharField(
                choices=[("simple", "Simple"), ("complex", "Complex")],
                default="simple",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="experimentsession",
            name="complexity_level",
            field=models.CharField(
                choices=[("simple", "Simple"), ("complex", "Complex")],
                default="simple",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="experimentsession",
            name="ear_order",
            field=models.CharField(
                choices=[("left_first", "Left First"), ("right_first", "Right First")],
                default="left_first",
                max_length=50,
            ),
        ),
    ]