from django.contrib import admin
from .models import Member, Emp,Dept, Master, Detail
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","phone","dob")

class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1

class MasterAdmin(admin.ModelAdmin):
    inlines = [DetailInline]

class EmpAdmin(admin.ModelAdmin):
    list_display = ("eName","gender","deptID")

admin.site.register(Master, MasterAdmin)
admin.site.register(Detail)

admin.site.register(Member, MemberAdmin)
admin.site.register(Emp, EmpAdmin)
admin.site.register(Dept)
