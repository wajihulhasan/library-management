
from django import forms

from authors.models import Author
from books.models import Book
from genres.models import Genre
from publishers.models import Publisher


class BookForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    publish_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
    author = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control"}), queryset=Author.objects.all(),empty_label="Please select author")
    publisher = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control"}), queryset=Publisher.objects.all(),empty_label="Please select Publisher")
    genre = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        queryset=Genre.objects.all()
    )
    isbn = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    quantity_available = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Book
        fields = "__all__"
