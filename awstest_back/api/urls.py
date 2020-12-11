from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.ResumeView.as_view(), name="resume"),
    path('resume/<int:pk>', views.ResumeDetailView.as_view(), name="resumedetail")
]