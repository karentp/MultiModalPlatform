import django_filters
from django_filters import DateFilter, CharFilter
from bootstrap_datepicker_plus import YearPickerInput
from django import forms
from .models import *
from django_filters.widgets import RangeWidget

class DateInput(forms.DateInput):
    input_type ='date'

class CorpusFilter(django_filters.FilterSet):
	start_date_publication = django_filters.DateFilter(field_name="start_date_publication", lookup_expr='year__gt', label ='Corpus con publicaciones después del año:')
								#widget= YearPickerInput())
	final_date_publication= DateFilter(field_name="final_date_publication", lookup_expr='lte', label='Corpus con publicaciones antes del año:')
	
	#final_date_publication=django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

	
	class Meta:
		model = Corpus
		#fields = {'gender':['exact'], 'start_date_publication':['exact'], 'final_date_publication':['exact', 'contains']}
		fields =['gender','start_date_publication','final_date_publication']
		labels = {
					'gender': 'Género',
					 'start_date_publication': 'Fecha de inicio de las publicaciones del corpus',
                  	'final_date_publication': 'Fecha final de las publicaciones del corpus',}

		widgets = {
            'start_date_publication': YearPickerInput(),
            'final_date_publication': YearPickerInput()
           
        }
		
class SegmentationFilter(django_filters.FilterSet):
	start_date_publication = DateFilter(field_name="start_date_publication", lookup_expr='gte')
	final_date_publication= DateFilter(field_name="final_date_publication", lookup_expr='lte')
	gender= CharFilter(field_name='gender', lookup_expr='icontains')


	class Meta:
		model = Segmentation
		fields = ['gender', 'start_date_publication', 'final_date_publication']
		