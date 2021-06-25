from django.contrib import admin
from .models import Customer, Mechanic, Request, Attendance, Feedback

# Register your models here.
admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Request)
admin.site.register(Attendance)
admin.site.register(Feedback)