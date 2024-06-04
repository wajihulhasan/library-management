from django import forms

from bookCopies.models import BookCopy
from books.models import Book


class BookCopiesForm(forms.ModelForm):
    acquisition_date = forms.DateField(widget=forms.SelectDateWidget())
    condition = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = BookCopy
        fields = "__all__"
