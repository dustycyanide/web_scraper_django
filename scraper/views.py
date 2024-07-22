from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LinkSubmission
from .serializers import LinkSubmissionSerializer

# Create your views here.

class SubmitLinkView(APIView):
    def post(self, request):
        print('received request to submit link')
        serializer = LinkSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('submit link request saved')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)