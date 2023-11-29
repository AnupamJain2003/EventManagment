from django.db import models


class Event(models.Model):
    eventId=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    about=models.CharField(max_length=2000)
    host=models.CharField(max_length=255)
    noOfStudents=models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=100)

class Halls(models.Model):
    HallId=models.IntegerField(primary_key=True)
    HallName=models.CharField(max_length=255)
    HallCapacity=models.IntegerField()
    HallStatus=models.CharField(choices={'Booked','Not Booked'})
class Student(models.Model):
    StudentId=models.IntegerField(primary_key=True)
    StudentName=models.CharField(max_length=255)
    StudentUI=models.CharField(max_length=255)
    StudentClass=models.CharField(max_length=255)
    StudentBranch=models.CharField(max_length=255)
    StudentCGPA=models.FloatField()
class Booking(models.Model):
    BookId=models.IntegerField(primary_key=True)
    EvntId=models.ForeignKey(Event.eventId,on_delete=models.CASCADE)
    HallId=models.ForeignKey(Halls.HallId,on_delete=models.CASCADE)

class CanteenOrder(models.Model):
    user_id = models.IntegerField()
    order_date = models.DateField()
    items = models.CharField(max_length=200)

class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=20)
    content = models.CharField(max_length=280)
