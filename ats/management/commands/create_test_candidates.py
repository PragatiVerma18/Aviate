from django.core.management.base import BaseCommand

from ats.models import Candidate


class Command(BaseCommand):
    help = "Create test candidates for the ATS"

    def handle(self, *args, **kwargs):
        test_data = [
            {
                "name": "Ajay Kumar Yadav",
                "age": 28,
                "gender": "Male",
                "email": "ajay.yadav@example.com",
                "phone_number": "9876543210",
            },
            {
                "name": "Ajay Kumar",
                "age": 30,
                "gender": "Male",
                "email": "ajay.kumar@example.com",
                "phone_number": "9876543211",
            },
            {
                "name": "Ajay Yadav",
                "age": 25,
                "gender": "Male",
                "email": "ajay.y@example.com",
                "phone_number": "9876543212",
            },
            {
                "name": "Kumar Yadav",
                "age": 32,
                "gender": "Male",
                "email": "kumar.yadav@example.com",
                "phone_number": "9876543213",
            },
            {
                "name": "Ramesh Yadav",
                "age": 29,
                "gender": "Male",
                "email": "ramesh.yadav@example.com",
                "phone_number": "9876543214",
            },
            {
                "name": "Ajay Singh",
                "age": 27,
                "gender": "Male",
                "email": "ajay.singh@example.com",
                "phone_number": "9876543215",
            },
        ]

        for data in test_data:
            Candidate.objects.update_or_create(email=data["email"], defaults=data)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {len(test_data)} test candidates!"
            )
        )
