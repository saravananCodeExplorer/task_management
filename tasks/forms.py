# Import Django's forms module
from django import forms

# Import Task model from models.py
from .models import Task


# Create a form based on the Task model
class TaskForm(forms.ModelForm):

    # Meta class contains form configuration
    class Meta:

        # Connect this form with the Task model
        model = Task

        # Fields that should be displayed in the form
        fields = [
            'title',
            'description',
            'status',
            'due_date',
        
        ]

        # Customize the HTML input fields
        widgets = {

            # Text input for task title
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task title'
                }
            ),

            # Textarea for task description
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task description',
                    'rows': 4
                }
            ),

            # Dropdown/select field for task status
            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            # Date picker for due date
            'due_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
    
        }


    # ==========================================
    # TITLE VALIDATION
    # ==========================================
    def clean_title(self):

        # Get the submitted title value
        title = self.cleaned_data['title']

        # Remove spaces and check whether title is empty
        if not title.strip():

            # Display validation error
            raise forms.ValidationError(
                "Title cannot be empty."
            )

        # Check minimum title length
        if len(title.strip()) < 3:

            # Display validation error
            raise forms.ValidationError(
                "Title must contain at least 3 characters."
            )

        # Return cleaned title
        return title.strip()


    # ==========================================
    # DESCRIPTION VALIDATION
    # ==========================================
    def clean_description(self):

        # Get the submitted description
        description = self.cleaned_data['description']

        # Check whether description is empty
        if not description.strip():

            # Display validation error
            raise forms.ValidationError(
                "Description cannot be empty."
            )

        # Return cleaned description
        return description.strip()