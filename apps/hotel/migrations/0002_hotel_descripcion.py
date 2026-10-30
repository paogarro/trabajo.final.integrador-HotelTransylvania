from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
