from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from BCN_App1.models import *


class StudentFeeDetailsAdmin(ImportExportModelAdmin):
    list_display = (
        'student_name', 'fathers_name', 'dob', 'gender', 'session_of_add', 'contact', 'branch',)
    search_fields = ('student_name',)


class FeesTransactionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'fathers_name', 'email', 'fee_type', 'fees_amount', 'dos')
    search_fields = ('student_name', 'fathers_name')


class FeesDetailsSessionWiseAdmin(admin.ModelAdmin):
    list_display = ('Session', 'date')


admin.site.register(FeesDetailsSessionWise, FeesDetailsSessionWiseAdmin,)
admin.site.register(StudentFeeDetails, StudentFeeDetailsAdmin,)
admin.site.register(FeesTransaction, FeesTransactionAdmin,)
admin.site.site_header = 'Admin | Bethany college of Nursing'
admin.site.index_title = 'Bethany college of Nursing'
admin.site.site_title = "Admin"
