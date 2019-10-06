from django.db import models
#from Notes.models import Notes_Table
# Create your models here.

# # Create your models here.
class Ticket_Table(models.Model):
    ph_no=models.IntegerField(null=True)
    firstname=models.CharField(max_length=25,default="")
    lastname=models.CharField(max_length=25,default="")
    city=models.CharField(max_length=25,default="")
    address=models.CharField(max_length=25,default="")
    Issuetype=models.CharField(max_length=50,default="")
    Issue_Desc=models.CharField(max_length=200,default="")
    Ticket_no=models.CharField(max_length=25,default="")
    Ticket_status=models.CharField(max_length=25,default="",null=True)

    def __str__(self):
        return self.Ticket_no

class Notes_Table(models.Model):
    Ticket_no=models.CharField(max_length=50)
    Ticket_notes=models.CharField(max_length=200,default="null")

    def __str__(self):
        return self.Ticket_no