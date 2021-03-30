from django import forms
from .models import Corpus
from bootstrap_datepicker_plus import DatePickerInput, YearPickerInput


class DateInput(forms.DateInput):
    input_type ='date'

class CorpusForm(forms.ModelForm):
    class Meta:
        model = Corpus
        fields = [
            'corpus_name', 'corpus_description', 'recollection_country', 
            'gender', 'corpus_pdf','corpus_document', 'start_date_publication', 'final_date_publication']
        
        labels = {'corpus_name': "Nombre del corpus" ,
                  'corpus_description': 'Descripción del Corpus',
                  'recollection_country': 'Países de recolección',
                  'gender': 'Género del Corpus',
                  'corpus_pdf': 'Documento informativo del corpus',
                  'corpus_document': 'Documento con las imágenes y segmentos del corpus',
                  'start_date_publication': 'Fecha de inicio de las publicaciones del corpus',
                  'final_date_publication': 'Fecha final de las publicaciones del corpus',}
        
        widgets = {
            'corpus_name': forms.TextInput(attrs={'class': 'form-control'}),
            'corpus_description': forms.TextInput(attrs={'class': 'form-control', 'type':'text-area'}),
            'recollection_country': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'corpus_pdf': forms.TextInput(attrs={'class': 'form-control', 'type':"file"}),
            'corpus_document': forms.TextInput(attrs={'class': 'form-control', 'type':"file"}),
            'start_date_publication': YearPickerInput(),
            'final_date_publication': YearPickerInput()
    
           
        }

class CorpusFormView(forms.ModelForm):
    class Meta:
        model = Corpus
        fields = [
            'corpus_name', 'corpus_description', 'recollection_country', 
            'gender', 'start_date_publication', 'final_date_publication']
        
        labels = {'corpus_name': "Nombre del corpus" ,
                  'corpus_description': 'Descripción del Corpus',
                  'recollection_country': 'Países de recolección',
                  'gender': 'Género del Corpus',
                  'corpus_pdf': 'Documento informativo del corpus',
                  'corpus_document': 'Documento con las imágenes y segmentos del corpus',
                  'start_date_publication': 'Fecha de inicio de las publicaciones del corpus',
                  'final_date_publication': 'Fecha final de las publicaciones del corpus',}
        
        widgets = {
            'corpus_name': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'corpus_description': forms.TextInput(attrs={'class': 'form-control', 'type':'text-area', 'disabled': True}),
            'recollection_country': forms.Select(attrs={'class': 'form-control', 'disabled': True}),
            'gender': forms.Select(attrs={'class': 'form-control', 'disabled': True}),
            'start_date_publication': YearPickerInput(attrs={'disabled': True}),
            'final_date_publication': YearPickerInput(attrs={'disabled': True})
    
           
        }