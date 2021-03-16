from django import forms
from .models import Corpus

class CorpusForm(forms.ModelForm):
    class Meta:
        model = Corpus
        labels ={ "corpus_name":"Nombre del corpus"}
        fields = [
            'corpus_name', 'corpus_description', 'recollection_country', 
            'gender', 'corpus_document', 'start_date_publication', 'final_date_publication']