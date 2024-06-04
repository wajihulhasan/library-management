from django import forms

from genres.models import Genre


class GenreForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Genre
        fields = "__all__"
