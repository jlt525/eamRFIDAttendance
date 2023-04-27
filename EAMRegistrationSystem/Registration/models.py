# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sessionstudent(models.Model):
    registerid = models.AutoField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    sessionid = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='SessionID', blank=True, null=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    presentstatus = models.IntegerField(db_column='PresentStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SessionStudent'
        unique_together = (('sessionid', 'studentid', 'presentstatus'),)


class Sessions(models.Model):
    sessionid = models.IntegerField(db_column='SessionID', primary_key=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.
    sessionname = models.CharField(db_column='SessionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessions'


class Students(models.Model):
    studentid = models.IntegerField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardserial = models.CharField(db_column='CardSerial', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'
        unique_together = (('studentid', 'fullname', 'course', 'cardserial'),)


class Register(models.Model):
    roomid = models.IntegerField(blank=True, null=True)
    cardserial = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(blank = True, null = True)

    class Meta:
        managed = False
