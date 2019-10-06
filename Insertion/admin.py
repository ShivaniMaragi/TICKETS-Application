from django.contrib import admin
from .models import  Ticket_Table,Notes_Table

# Register your models here.
admin.site.register(Ticket_Table)
admin.site.register(Notes_Table)
