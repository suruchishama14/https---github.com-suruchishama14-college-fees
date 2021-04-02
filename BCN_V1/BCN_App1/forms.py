from django import forms
from .models import *


class FeesTransactionForm(forms.ModelForm):
    class Meta:
        model = FeesTransaction
        fields = "__all__"


class FeesDetailsSessionWiseForm(forms.ModelForm):
    class Meta:
        model = FeesDetailsSessionWise
        fields = "__all__"


class StudentFeeDetailsForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = StudentFeeDetails
        fields = "__all__"
