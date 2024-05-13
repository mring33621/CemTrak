import csv
from django.http import HttpResponse
from cemtrakapp.models import Organization, Emitter


def organizations_datadump(request):
    """
    Provides a CSV datadump of the Organization model.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="organizations.csv"'

    writer = csv.writer(response)
    # Write header row based on model fields
    org_fields = [f for f in Organization._meta.get_fields() if f.name != 'emitter']
    writer.writerow([f.name for f in org_fields])

    # Write data rows
    for obj in Organization.objects.all():
        writer.writerow([getattr(obj, f.name) for f in org_fields])

    return response


def emitters_datadump(request):
    """
    Provides a CSV datadump of the Emitter model.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emitters.csv"'

    writer = csv.writer(response)
    # Write header row based on model fields
    writer.writerow([f.name for f in Emitter._meta.get_fields() if f.model == Emitter])

    # Write data rows
    for obj in Emitter.objects.all():
        writer.writerow([getattr(obj, f.name) for f in Emitter._meta.get_fields() if f.model == Emitter])

    return response