from django.shortcuts import get_object_or_404, render

# Create your views here.

from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
#****************************************************************************************************************************************************
import spacy
nlp = spacy.load("en_pipeline")
import fitz

#cv = get_object_or_404(Candidate, id=6)
    
    # Path to the CV file
#cv_path = cv.file.path




def parse_cv(cv_path):
    import sys ,fitz
    doc=fitz.open(cv_path)
    text= ''
    for page in doc:
       text=text +str(page.get_text())

    text =text.strip()
    text="  ".join(text.split())

    doc=nlp(text)
    for ent in doc.ents:
      Parse= print(ent.label_, "    ->>>>>>",ent.text)

    return Parse

#x=parse_cv('media\cv_pdfs\Alice_Clark_CV_T5y3D7U.pdf')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .models import CV
#from .serializers import CVSerializer
#from django.utils import parse_cv  # Ensure to import the updated parse_cv function
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
#from .utils import parse_cv  # Ensure the updated parse_cv function is imported

class ParseCVView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        cv_path = request.data.get('cv')

        if not name or not cv_path:
            return Response({"error": "Name or CV path not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            parsed_entities = parse_cv(cv_path)
            return Response({
                "parsed_entities": parsed_entities,
                "cv_path": cv_path
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    # def post(self, request, *args, **kwargs):
    #     cv_path = request.data.get('cv_path')
    #     if not cv_path:
    #         return Response({"error": "CV path not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
    #     try:
    #         parsed_entities = parse_cv(cv_path)
    #         return Response({"parsed_entities": parsed_entities}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

