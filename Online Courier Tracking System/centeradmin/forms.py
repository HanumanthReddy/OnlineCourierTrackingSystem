__author__ = 'srikanth'

from django import forms
from centeradmin.models import online_data

class OnlineForm(forms.ModelForm):

    OPTIONS = (
        ("General Items", "General Items"),
        ("Perishable Items", "Perishable Items"),
        ("Electronic Goods", "Electronic Goods"),
        ("Suitcases, Travel Bags", "Suitcases, Travel Bags"),
        ("Leisure Items","Leisure Items"),
        ("Sport Items","Sport Items"),
        ("Large Items","Large Items"),
        ("Small House Hold Items","Small House Hold Items"),
        ("Works of Art","Works of Art"),
    )

    WEIGHTS =(
        ("Below 1 Kg.","Below 1 Kg."),
        ("1 Kg - 5 Kgs","1 Kg - 5 Kgs"),
        ("1 Kg - 5 Kgs","1 Kg - 5 Kgs"),
        ("10 Kg - 50 Kgs","10 Kg - 50 Kgs"),
        ("50 Kg - 100 Kgs","50 Kg - 100 Kgs"),
        ("Above 100 Kgs ","Above 100 Kgs "),
    )

    ptype = forms.MultipleChoiceField(widget=forms.ChoiceField(OPTIONS)) #CheckboxSelectMultiple,choices=OPTIONS)
    pweight = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=WEIGHTS)
    pmail = forms.EmailField(max_length=128)
    paddress = forms.CharField(widget=forms.Textarea)
    pmobile = forms.CharField(max_length=128)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = online_data
        fields = ('ptype','pweight','pmail','paddress','pmobile',)

