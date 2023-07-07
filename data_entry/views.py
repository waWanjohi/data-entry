from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from data_entry.api_utils import APIList, APIDetail
from rest_framework.viewsets import ReadOnlyModelViewSet
from data_entry.models import CustomEntry, Category, HealthInstitutionEntry, ProfessionEntry, EventEntry
from data_entry.serializers import CustomEntrySerializer, CategorySerializer, HealthInstitutionEntrySerializer, \
    ProfessionEntrySerializer, EventEntrySerializer


class CustomEntryList(APIList):
    """
    List all custom entries
    """

    model_class = CustomEntry
    serializer_class = CustomEntrySerializer


class CustomEntryDetail(APIDetail):
    """
    Get a single Custom Entry
    """

    model_class = CustomEntry
    serializer_class = CustomEntrySerializer


class CategoryList(APIList):
    """
    List all categories
    """

    model_class = Category
    serializer_class = CategorySerializer


class CategoryDetail(APIDetail):
    """
    Get a single Category
    """

    model_class = Category
    serializer_class = CategorySerializer


class HealthInstitutionEntryList(APIList):
    """
    Get Health Institution Entries as a paginated list
    """

    model_class = HealthInstitutionEntry
    serializer_class = HealthInstitutionEntrySerializer


class HealthInstitutionEntryDetail(APIDetail):
    """
    Get a single Health Institution Entry
    """
    model_class = HealthInstitutionEntry
    serializer_class = HealthInstitutionEntrySerializer


class ProfessionEntryList(APIList):
    """
    Get Profession Entries as a paginated list
    """
    model_class = ProfessionEntry
    serializer_class = ProfessionEntrySerializer


class ProfessionEntryDetail(APIDetail):
    """
    Get a single Profession Entry
    """
    model_class = ProfessionEntry
    serializer_class = ProfessionEntrySerializer


class EventEntryList(APIList):
    """
    Get Event Entries as a paginated list
    """
    model_class = EventEntry
    serializer_class = EventEntrySerializer


class EventEntryDetail(APIDetail):
    """
    Get a single Event Entry
    """
    model_class = EventEntry
    serializer_class = EventEntrySerializer


"""
Add Filter Endpoints for the API
"""


class HealthInstitutionEntryFilter(ReadOnlyModelViewSet):
    """
    Get filters used in filtering against
    HealthInstitutionEntryList APIs
    """

    queryset = HealthInstitutionEntry.objects.prefetch_related().all()
    serializer_class = HealthInstitutionEntrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name", "id")


class EventEntryFilter(ReadOnlyModelViewSet):
    """
    Get filters used in filtering against
    EventEntryList APIs
    """
    queryset = EventEntry.objects.prefetch_related().all()
    serializer_class = EventEntrySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("event_name", "id")


class ProfessionEntryFilter(ReadOnlyModelViewSet):
    """
    Get filters used in filtering against
    ProfessionEntryList APIs
    """
    queryset = ProfessionEntry.objects.prefetch_related().all()
    serializer_class = ProfessionEntrySerializer
    filterset_fields = ("name", "occupation", "id")


class CategoryFilter(ReadOnlyModelViewSet):
    """
    Get filters used in filtering against
    CustomEntryList APIs
    """
    queryset = Category.objects.prefetch_related().all()
    serializer_class = CategorySerializer
    filterset_fields = ("name", "id")


class CustomEntryFilter(ReadOnlyModelViewSet):
    """
    List all custom entries
    """

    queryset = CustomEntry.objects.prefetch_related().all()
    serializer_class = CustomEntrySerializer
    filterset_fields = ("name", "id")
