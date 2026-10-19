from django.db import migrations

from questions.exam_structures import EXAM_STRUCTURES


def load(apps, schema_editor):
    model = apps.get_model('questions', 'ExamStructure')
    model.objects.all().delete()
    model.objects.bulk_create([
        model(certification=c, version=v, title=t, num_questions=n,
              total_points=p, passing_score=s, minutes=m, minutes_extended=x, order=i)
        for i, (c, v, t, n, p, s, m, x) in enumerate(EXAM_STRUCTURES)
    ])


class Migration(migrations.Migration):

    dependencies = [('questions', '0006_examstructure')]

    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
