from rest_framework import serializers
from resume_api.models import Profile, WorkExperience, Education, Skills


# For serializing profile section
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "address", "email", "contact_number"]


# For serializing work experience section
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = [
            "company_name",
            "job_title",
            "job_description",
            "duration",
            "location",
        ]


# For serializing education section
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["university_name", "degree", "graduation_date", "university_address"]


# For serializing skills section
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["name"]
