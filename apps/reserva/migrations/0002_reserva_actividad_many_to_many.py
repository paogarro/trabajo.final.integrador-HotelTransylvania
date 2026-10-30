from django.db import migrations, models


def copy_activity_relationships(apps, schema_editor):
    Reserva = apps.get_model('reserva', 'Reserva')
    database = schema_editor.connection.alias
    for reserva in Reserva.objects.using(database).all().iterator():
        if reserva.actividad_turistica_anterior_id:
            reserva.actividad_turistica.add(reserva.actividad_turistica_anterior_id)


def restore_activity_relationships(apps, schema_editor):
    Reserva = apps.get_model('reserva', 'Reserva')
    database = schema_editor.connection.alias
    for reserva in Reserva.objects.using(database).all().iterator():
        actividad = reserva.actividad_turistica.first()
        if actividad:
            reserva.actividad_turistica_anterior_id = actividad.pk
            reserva.save(using=database, update_fields=['actividad_turistica_anterior'])


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='actividad_turistica',
            new_name='actividad_turistica_anterior',
        ),
        migrations.AddField(
            model_name='reserva',
            name='actividad_turistica',
            field=models.ManyToManyField(
                blank=True,
                related_name='reservas',
                to='actividad_turistica.actividadturistica',
            ),
        ),
        migrations.RunPython(
            copy_activity_relationships,
            restore_activity_relationships,
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='actividad_turistica_anterior',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_reserva',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='total',
        ),
    ]
