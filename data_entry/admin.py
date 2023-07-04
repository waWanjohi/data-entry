from django.contrib import admin

from data_entry.models import (Category,
                               CustomEntry,
                               ProfessionEntry,
                               HealthInstitutionEntry,
                               EventEntry,
                               )

admin.site.register(Category)
admin.site.register(CustomEntry)
admin.site.register(ProfessionEntry)
admin.site.register(HealthInstitutionEntry)
admin.site.register(EventEntry)
