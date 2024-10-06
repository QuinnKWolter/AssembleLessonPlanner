from django import forms
from .models import (
    LessonPlan, InventoryItem, InventoryTransaction, MaterialPreparation
)
from django.forms import inlineformset_factory

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duration': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'preparation_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ['quantity', 'notes']

class MaterialPreparationForm(forms.ModelForm):
    class Meta:
        model = MaterialPreparation
        fields = ['inventory_item', 'quantity_needed']

MaterialPreparationFormSet = inlineformset_factory(
    LessonPlan, MaterialPreparation, form=MaterialPreparationForm,
    fields=['inventory_item', 'quantity_needed'],
    extra=1, can_delete=True
)