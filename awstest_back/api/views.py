from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
from datetime import datetime


class ResumeView(generics.ListCreateAPIView):
    # RESUME GET 정보가져오기
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    # RESUME 생성
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        taskname = request.data['taskname']
        targettask = Task.objects.get(name=taskname)
        if serializer.is_valid(raise_exception=True):
            resume = serializer.save(user=request.user,task_id=targettask.id)
        images = dict((request.data).lists())['image']
        for image in images:
            imageSerializer = ResumeImageSerializer(data={'image':image})
            if imageSerializer.is_valid(raise_exception=True):
                imageSerializer.save(resume_id=resume.id)
        return Response({'data':True})

class ResumeDetailView(APIView):
    def get_object(self, pk):
        try:
            return Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            raise Http404
    
    # Resume 디테일
    def get(self, request, pk):
        resume = self.get_object(pk)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data)
    
    # Resume 삭제
    def delete(self, request, pk):
        resume = self.get_object(pk)
        if resume.user == request.user:
            resume.delete()
            return Response({"messgae": "삭제 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # resume 수정
    def put(self, request, pk):
        resume = self.get_object(pk)
        if resume.user == request.user:
            serializer = ResumeSerializer(resume, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
