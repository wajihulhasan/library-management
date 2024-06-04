
from django import forms

from bookReviews.models import BookReview


class BookReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(min_value=0, max_value=5)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = BookReview
        fields = '__all__'
