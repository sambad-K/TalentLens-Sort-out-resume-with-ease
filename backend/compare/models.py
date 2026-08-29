from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):

    class JobType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        CONTRACT = "CONTRACT", "Contract"
        INTERNSHIP = "INTERNSHIP", "Internship"
        FREELANCE = "FREELANCE", "Freelance"

    title = models.CharField(
        max_length=200
    )

    experience = models.CharField(
        max_length=100,
        help_text="Example: 2-4 years"
    )

    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices
    )

    qualification = models.TextField()

    required_skills = models.TextField(
        help_text="Comma-separated skills"
    )
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title