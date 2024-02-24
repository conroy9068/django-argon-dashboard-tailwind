from django import forms

from .models import Assessment, RepairItem, Vehicle


class Meta:
    model = Vehicle
    fields = ['make', 'model', 'spec', 'reg_no', 'color', 'vin', 'engine_no']
    # ... include other fields as per form

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['engineer_name', 'date', 'membership_number']
        # ... include other fields as per form

class RepairItemForm(forms.ModelForm):
    class Meta:
        model = RepairItem
        fields = ['description', 'action']
        # ... include other fields as per form
