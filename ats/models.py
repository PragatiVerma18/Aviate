from ulid2 import generate_ulid_as_uuid

from django.db import models
from django.utils import timezone


class Candidate(models.Model):
    GENDER_MALE = "MALE"
    GENDER_FEMALE = "FEMALE"
    GENDER_OTHER = "OTHER"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ]

    id = models.UUIDField(
        primary_key=True, default=generate_ulid_as_uuid, editable=False
    )
    name = models.CharField(max_length=255, db_index=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
