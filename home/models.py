from django.contrib.gis.db import models
from django.contrib.auth.models import User


# class Barangay(models.Model):
#     Name = models.CharField(max_length=255, unique=True)
#     Location = models.PointField(blank=True, null=True)
#
#     def IncidentCount(self):
#         return self.incident_set.count()
#
#     def IncidentInstances(self):
#         return self.incident_set.all()
#
#     def __str__(self):
#         return self.Name

class Barangay(models.Model):
    Name = models.CharField(max_length=75)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True)

    def IncidentCount(self):
        return self.incident_set.count()

    def IncidentInstances(self):
        return self.incident_set.all()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name',)


class InvestigatorRank(models.Model):
    Code = models.CharField(max_length=100, unique=True)
    Definition = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.Code


class Investigator(models.Model):
    FirstName = models.CharField(max_length=100, blank=True, null=True)
    MiddleName = models.CharField(max_length=100, blank=True, null=True)
    LastName = models.CharField(max_length=100)
    Rank = models.ForeignKey(InvestigatorRank,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        delimeter = ' '
        FullName = [self.Rank, self.FirstName, self.MiddleName, self.LastName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)

    class Meta:
        unique_together = (('FirstName', 'LastName'),)


class Incident(models.Model):
    DateTime = models.DateTimeField()
    HouseNumber = models.CharField(max_length=255,blank=True, null=True)
    Street = models.CharField(max_length=255,blank=True, null=True)
    Barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True, blank=True)
    Location = models.PointField(blank=True, null=True)
    OwnerName = models.CharField(max_length=255, blank=True, null=True)
    EstablishmentName = models.CharField(max_length=255, blank=True, null=True)
    OccupancyType = models.CharField(max_length=255,blank=True, null=True)
    ALARM_LEVEL_CHOICES = [
        ('1','1'),
        ('2', '2'),
        ('3', '3'),
    ]
    AlarmLevel = models.CharField(max_length=1, choices=ALARM_LEVEL_CHOICES, default='1')
    Injuries = models.IntegerField(default=0)
    FatalitiesMale = models.IntegerField(default=0)
    FatalitiesFemale = models.IntegerField(default=0)
    EstimatedDamageCost = models.IntegerField(default=0)
    FinalDamageCost = models.IntegerField(default=0)
    Origin = models.CharField(max_length=255, blank=True, null=True)
    Cause = models.TextField(blank=True, null=True)
    FireArsonInvestigator = models.ForeignKey(Investigator, on_delete=models.SET_NULL, null=True, blank=True)
    REMARKS_CHOICES = [
        ('closed', 'Closed'),
        ('under investigation', 'Under Investigation'),
        ('',''),
    ]

    Remarks = models.CharField(max_length=255, choices=REMARKS_CHOICES, default='closed', blank=True)
    Notes = models.TextField(default="", blank=True, null=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        delimeter = ' '
        FullName = [self.DateTime, self.OwnerName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)
    
    class Meta:
        unique_together = (('DateTime', 'OwnerName',),)
        ordering = ('-DateTime','Barangay',)



