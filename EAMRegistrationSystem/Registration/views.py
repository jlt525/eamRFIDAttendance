from datetime import time
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from Registration.models import Register, Sessionstudent, Sessions, Students
from Registration.serializers import RegisterSerializer, SessionstudentSerializer, SessionSerializer, StudentSerializer

class StudentsList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['studentid', 'fullname', 'course']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SessionsList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionSerializer
    filterset_fields = ['sessionid', 'roomid', 'sessionname', 'date', 'starttime', 'endtime']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SessionDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SessionstudentsList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Sessionstudent.objects.all()
    serializer_class = SessionstudentSerializer
    filterset_fields = ['sessionid', 'studentid', 'presentstatus']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SessionstudentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Sessionstudent.objects.all()
    serializer_class = SessionstudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class RegisterAttendance(APIView):
    def post(self, request, format = None):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            roomid = serializer.data['roomid']
            cardserial = serializer.data['cardserial']
            timestamp = serializer.data['timestamp'].strip("Z")
            date = timestamp.split("T")[0]
            inTime = timestamp.split("T")[1].split(":")
            starttime = time(int(inTime[0]))

            sessionid = Sessions.objects.get(roomid = roomid, date = date, starttime = starttime).sessionid
            studentid = Students.objects.get(cardserial = cardserial).studentid

            sessionStudentSerializer = SessionstudentSerializer(data = {'sessionid': sessionid, 'studentid': studentid, 'presentstatus': 1})

            sessionStudentSerializer.is_valid()
            sessionStudentSerializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return  Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
