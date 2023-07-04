from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_created=True, auto_now=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_created=True, auto_now=True, auto_now_add=False
    )

    class Meta:
        abstract = True


class Category(BaseModel):
    """A dynamic Category. This will be used to create a custom entry model"""
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()


class HealthInstitutionEntry(BaseModel):
    """ Boilerplate fields for a generic Health Institution. """

    name = models.CharField(max_length=50, unique=True, null=False)
    phone_number = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50, unique=True)
    official_email_address = models.EmailField(unique=True)


class ProfessionEntry(BaseModel):
    """ Boilerplate fields for a generic Profession. """

    name = models.CharField(max_length=50, unique=True, )
    description = models.TextField(null=False)
    occupation = models.CharField(max_length=50, unique=True)
    minimum_entry_age = models.PositiveIntegerField(unique=True)
    is_gender_agnostic = models.BooleanField(default=True)


class EventEntry(BaseModel):
    """ Boilerplate fields for a generic Event. """

    event_name = models.CharField(max_length=30, unique=True, null=False)
    location = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    event_date = models.DateTimeField(null=False)
    event_organizer_email = models.EmailField(unique=True)


class CustomEntry(BaseModel):
    """ Fields to cater for dynamic category entries. """

    STATUS = (
        ('NEW', 'NEW'),
        ('UNDER_REVIEW', 'UNDER_REVIEW'),
        ('PUBLISHED', 'PUBLISHED'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="assigned_entries")
    attachment = models.URLField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='NEW', max_length=50)

    class Meta:
        unique_together = ("category", "name")
