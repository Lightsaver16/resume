# Using Class View
from rest_framework.views import APIView
from resume_api.models import Profile, WorkExperience, Education, Skills
from resume_api.serializers import (
    ProfileSerializer,
    WorkExperienceSerializer,
    EducationSerializer,
    SkillsSerializer,
)
from rest_framework.response import Response
from rest_framework import status


# Get Resume
class ResumeView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        work_experience = WorkExperience.objects.all()
        education = Education.objects.first()
        skills = Skills.objects.all()

        profile_data = ProfileSerializer(profile).data
        work_experience = WorkExperienceSerializer(work_experience, many=True).data
        education_data = EducationSerializer(education).data
        skills_data = SkillsSerializer(skills, many=True).data

        resume_data = {
            "profile": profile_data,
            "work_experience": work_experience,
            "education": education_data,
            "skills": skills_data,
        }

        return Response(resume_data, status=status.HTTP_200_OK)


class ResumeCreate(APIView):
    def post(self, request):
        profile_data = request.data.get("profile")
        work_experience_data = request.data.get("work_experience")
        education_data = request.data.get("education")
        skills_data = request.data.get("skills")

        profile_serializer = ProfileSerializer(data=profile_data)
        if not profile_serializer.is_valid():
            return Response(
                profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        profile = profile_serializer.save()

        # Check if the work_experience payload is valid, if not, will delete previous
        # payload(e.g. profile).
        work_experience_serializer = WorkExperienceSerializer(
            data=work_experience_data, many=True
        )
        if not work_experience_serializer.is_valid():
            profile.delete()
            return Response(
                work_experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        work_experience = work_experience_serializer.save()

        # Check if the education payload is valid, if not, will delete previous
        # payload(e.g. profile, work experience)
        education_serializer = EducationSerializer(data=education_data)
        if not education_serializer.is_valid():
            profile.delete()
            for work in work_experience:
                work.delete()
            return Response(
                education_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        education = education_serializer.save()

        # Check if the skills payload is valid, if not, will delete previous
        # payload(e.g. profile, work experience, education)
        skills_serializer = SkillsSerializer(data=skills_data, many=True)
        if not skills_serializer.is_valid():
            profile.delete()
            for work in work_experience:
                work.delete()
            education.delete()
            return Response(
                skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        skills = skills_serializer.save()

        # Re-serializing data to throw as a response upon saving via POST request
        resume_data = {
            "profile": ProfileSerializer(profile).data,
            "work_experience": WorkExperienceSerializer(
                work_experience, many=True
            ).data,
            "education": EducationSerializer(education).data,
            "skills": SkillsSerializer(skills, many=True).data,
        }

        return Response(resume_data, status=status.HTTP_201_CREATED)
