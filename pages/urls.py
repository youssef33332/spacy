from django.urls import path 
from . import views


from django.urls import path
from .views import CandidateListCreateAPIView, CandidateRetrieveUpdateDestroyAPIView, ParseCVView

urlpatterns = [
    path('candidates/', CandidateListCreateAPIView.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateRetrieveUpdateDestroyAPIView.as_view(), name='candidate-retrieve-update-destroy'),
    path('api/parse-cv/', ParseCVView.as_view(), name='parse_cv'),
]
