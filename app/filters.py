import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CorpusFilter(django_filters.FilterSet):
	start_date_publication = DateFilter(field_name="start_date_publication", lookup_expr='gte')
	final_date_publication= DateFilter(field_name="final_date_publication", lookup_expr='lte')
	gender= CharFilter(field_name='gender', lookup_expr='icontains')


	class Meta:
		model = Corpus
		fields = ['gender', 'start_date_publication', 'final_date_publication']

class SegmentationFilter(django_filters.FilterSet):
	start_date_publication = DateFilter(field_name="start_date_publication", lookup_expr='gte')
	final_date_publication= DateFilter(field_name="final_date_publication", lookup_expr='lte')
	gender= CharFilter(field_name='gender', lookup_expr='icontains')


	class Meta:
		model = Segmentation
		fields = ['gender', 'start_date_publication', 'final_date_publication']
		