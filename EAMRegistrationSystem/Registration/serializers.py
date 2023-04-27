from rest_framework import serializers
from Registration.models import Register, Sessionstudent, Sessions, Students

class SessionstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessionstudent
        fields = ['registerid', 'sessionid', 'studentid', 'presentstatus']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = ['sessionid', 'roomid', 'sessionname', 'date', 'starttime', 'endtime']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['studentid', 'fullname', 'course', 'cardserial']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['roomid', 'cardserial', 'timestamp']
