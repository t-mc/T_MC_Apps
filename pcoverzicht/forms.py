from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab

from .models import Computer, Software

class ComputerForm(forms.Form):
    naam = forms.CharField()
    gebruiker = forms.CharField()
    merkentype = forms.CharField()
    kenmerken = forms.CharField(widget=forms.Textarea)
    aanschafdatum = forms.DateField(widget=forms.SelectDateWidget)
    serienummer = forms.CharField()

    helper = FormHelper()
    helper.form_tag = True
    helper.layout = Layout(
        TabHolder (
            Tab(
                'PC Naam en gebruiker',
                'naam',
                'gebruiker'
            ),
            Tab(
                'Type en aankoopdatum',
                'merkentype',
                'kenmerken',
                'aanschafdatum',
                'serienummer'
            )
        ),
        ButtonHolder(
            Submit('submit', 'Opslaan', css_class='btn btn-primary')
        )
    )


    class Meta:
        model = Computer
        # fields = ['naam', 'gebruiker', 'merkentype', 'kenmerken', 'aanschafdatum', 'serienummer']



# class SoftwareForm(forms.ModelForm):
#
#     class Meta:
#
#         model = Software



