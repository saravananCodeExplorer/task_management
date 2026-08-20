from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task description',
                    'rows': 4
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title.strip():
            raise forms.ValidationError(
                "Title cannot be empty."
            )

        if len(title.strip()) < 3:
            raise forms.ValidationError(
                "Title must contain at least 3 characters."
            )

        return title.strip()

    def clean_description(self):
        description = self.cleaned_data['description']

        if not description.strip():
            raise forms.ValidationError(
                "Description cannot be empty."
            )

        return description.strip()