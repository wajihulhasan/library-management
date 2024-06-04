from django import forms

from authors.models import Author


class AuthorForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Name", "class": "form-control"})
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "style": "height: 100px; display: flex;"}
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date",'class': 'form-control'}),
        help_text="Please enter the date of birth in YYYY-MM-DD format.",
    )
    nationality = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Nationality", "class": "form-control"}
        )
    )

    class Meta:
        model = Author
        fields = "__all__"
