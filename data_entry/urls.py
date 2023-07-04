from django.urls import path
from rest_framework.routers import DefaultRouter

from data_entry.views import (CustomEntryList, CategoryList, CustomEntryDetail, CategoryDetail,
                              HealthInstitutionEntryList, HealthInstitutionEntryDetail, ProfessionEntryList,
                              ProfessionEntryDetail,
                              EventEntryList, EventEntryDetail, HealthInstitutionEntryFilter, CategoryFilter,
                              ProfessionEntryFilter, EventEntryFilter, CustomEntryFilter)

router = DefaultRouter()

router.register(r"health-institutions-filter", HealthInstitutionEntryFilter, basename="health-institutions")
router.register('categories-filter', CategoryFilter, basename="categories"),
router.register('custom-categories-filter', CustomEntryFilter, basename="custom-categories"),
router.register('professional-details-filter', ProfessionEntryFilter, basename='professional-details')
router.register('event-details-filter', EventEntryFilter, basename='events')

urlpatterns = [

                  path('categories/', CategoryList.as_view()),
                  path('categories/<int:pk>', CategoryDetail.as_view()),
                  path('custom-categories/', CustomEntryList.as_view()),
                  path('custom-categories/<int:pk>', CustomEntryDetail.as_view()),

                  path('health-institutions/', HealthInstitutionEntryList.as_view()),
                  path('health-institutions/<int:pk>', HealthInstitutionEntryDetail.as_view()),
                  path('professional-details/', ProfessionEntryList.as_view()),
                  path('professional-details/<int:pk>', ProfessionEntryDetail.as_view()),
                  path('event-details/', EventEntryList.as_view()),
                  path('event-details/<int:pk>', EventEntryDetail.as_view()),
              ] + router.urls
