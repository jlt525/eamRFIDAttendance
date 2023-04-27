from django.contrib import admin
from Registration.models import Sessionstudent, Sessions, Students

class SessionsAdmin(admin.ModelAdmin):
    list_display = ("sessionid", "sessionname", "date", "starttime", "roomid")

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("studentid", "fullname", "course")

class SessionstudentAdmin(admin.ModelAdmin):
    list_display = ("studentid", "sessionid", "presentstatus")

admin.site.register(Sessionstudent, SessionstudentAdmin)
admin.site.register(Sessions, SessionsAdmin)
admin.site.register(Students, StudentsAdmin)
