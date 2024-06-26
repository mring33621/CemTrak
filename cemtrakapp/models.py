from django.db import models


class MeasurementUnit(models.TextChoices):
    GCO2EQ_KWH = 'gCO2eq/kWh'
    KT = 'kt'
    MT_CO2E = 'MtCO2e'
    MG = 'Mg'


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Emitter(models.Model):
    name = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255, unique=True)
    # emitters add carbon to the atmosphere; compensators remove carbon from the atmosphere
    is_compensator = models.BooleanField(default=False)
    measurement_unit = models.CharField(
        max_length=20,
        choices=MeasurementUnit.choices,
        default=MeasurementUnit.MT_CO2E
    )
    high_measurement_amt = models.DecimalField(max_digits=10, decimal_places=2)
    med_measurement_amt = models.DecimalField(max_digits=10, decimal_places=2)
    low_measurement_amt = models.DecimalField(max_digits=10, decimal_places=2)
    off_measurement_amt = models.DecimalField(max_digits=10, decimal_places=2)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.external_id} -- {self.organization} -- {self.name}'
