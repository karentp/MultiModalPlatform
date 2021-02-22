import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class SegmentationFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="created_at", lookup_expr='gte')
	end_date = DateFilter(field_name="created_at", lookup_expr='lte')
	document_name= CharFilter(field_name='document_name', lookup_expr='icontains')


	class Meta:
		model = Segmentation
		fields = '__all__'
		exclude = ['image', 'created_at', 'updated_at']