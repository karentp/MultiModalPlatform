from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Segmentation)

class SegmentationAdmin(ImportExportModelAdmin):
    list_display =('image','document_name','code','created_by')
