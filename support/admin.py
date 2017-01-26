from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import UserProfile, Cases, Activiteiten, CaseStatus, ActivityStatus, ActivityType

class CaseActivities(admin.TabularInline):
    model = Activiteiten
    extra = 1

class CasesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['klant', 'contactpersoon', 'onderwerp']}),
        ("Detail informatie", {'fields': ['status', 'omschrijving', 'datumMelding', 'uitvoerende']})
    ]
    inlines = [
        CaseActivities
    ]
    list_display= ('onderwerp', 'omschrijving', 'datumMelding', 'status', 'klant', 'contactpersoon', 'uitvoerende')
    list_filter = ('status', 'klant')

class ActiviteitenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('caseId', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datumUitgevoerd')

#
# Register your models here.
#
admin.site.register(UserProfile)
admin.site.register(Cases, CasesAdmin)
admin.site.register(Activiteiten, ActiviteitenAdmin)
admin.site.register(CaseStatus)
admin.site.register(ActivityStatus)
admin.site.register(ActivityType)






