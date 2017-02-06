from django.db import models, IntegrityError
from django.conf import settings
from datetime import date
import random
import string
from .usermodels import User


#
# Lookup tabel voor case status
#
class CaseStatus(models.Model):
    status = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Case statussen'

    def __str__(self):
        return self.status

#
# Lookup tabel voor activiteit status
#
class ActivityStatus(models.Model):
    status = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit statussen'

    def __str__(self):
        return self.status

#
# Lookup tabel voor activiteit soorten
#
class ActivityType(models.Model):
    type = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit typen'

    def __str__(self):
        return self.type

#
# Record layout cases tabel
#
class Cases(models.Model):
    slug = models.CharField(max_length=16, primary_key=True, editable=False, unique=True)
    onderwerp = models.CharField(max_length=64)
    omschrijving = models.TextField()
    datumMelding = models.DateField(("Datum melding"), default=date.today)
    datumGereed = models.DateField(("Datum gereed"), blank=True, null=True)
    status = models.ForeignKey(CaseStatus, null=True)
    klant = models.CharField(max_length=64, null=True)
    contactpersoon = models.CharField(max_length=64, blank=True, null=True)
    uitvoerende = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = id_generator()
            # using your function as above or anything else
        success = False
        failures = 0
        while not success:
            try:
                super(Cases, self).save(*args, **kwargs)
            except IntegrityError:
                 failures += 1
                 if failures > 5: # or some other arbitrary cutoff point at which things are clearly wrong
                     raise
                 else:
                     # looks like a collision, try another random value
                     self.auto_pseudoid = id_generator()
            else:
                 success = True

#
# Record layout voor activiteiten tabel
#
class Activiteiten(models.Model):
    caseId = models.ForeignKey(Cases)
    activiteit = models.ForeignKey(ActivityType)
    status = models.ForeignKey(ActivityStatus)
    omschrijving = models.TextField()
    uitvoerende = models.CharField(max_length=64, blank=True, null=True)
    datumUitgevoerd = models.DateField(("Datum"), default=date.today)

    class Meta:
        verbose_name_plural = 'Activiteiten'

    # def __str__(self):
    #     return self.activiteit


#
# Functie voor het genereren van alfanumerieke case code
#
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

