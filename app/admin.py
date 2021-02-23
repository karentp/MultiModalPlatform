from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Segmentation)

class SegmentationAdmin(ImportExportModelAdmin):
    list_display =('image','document_name','code','created_by')

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','institute')

