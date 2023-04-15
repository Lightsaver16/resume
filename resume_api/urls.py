from django.contrib import admin
from django.urls import path
from resume_api.views import ResumeView, ResumeCreate

urlpatterns = [path("", ResumeView.as_view()), path("create", ResumeCreate.as_view())]
