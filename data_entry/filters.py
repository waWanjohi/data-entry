import django_filters

from data_entry.models import HealthInstitutionEntry


class HealthInstitutionEntryFilter(django_filters.FilterSet):
    class Meta:
        model = HealthInstitutionEntry
        fields = ("name", "phone_number", "country", "official_email_address")
