from rest_framework import serializers

from data_entry.models import EventEntry, ProfessionEntry, HealthInstitutionEntry, CustomEntry, Category


class EventEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventEntry
        fields = ("event_name", "location", "event_date", "description", "event_organizer_email")


class ProfessionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionEntry
        fields = ("name", "description", "occupation", "minimum_entry_age", "is_gender_agnostic")


class HealthInstitutionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInstitutionEntry
        fields = ("name", "phone_number", "country", "official_email_address")


class CustomEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomEntry
        fields = ("name", "category", "description", "assigned_to", "attachment")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "description")
