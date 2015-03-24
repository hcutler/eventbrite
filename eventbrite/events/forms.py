from django import forms
from .models import Category


class CategorySelectForm(forms.Form):
    """
        Form for user to select 3 interested categories
    """
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(),
                                              required=True)

    def clean_category(self):
        categories = self.cleaned_data['category']
        if len(categories) != 3:
            raise forms.ValidationError('Please select exactly 3 categories')
        return categories
