from django.urls import path
from .views import (
    LoanListView,
    LoanDetailView,
    LoanCreateView,
    LoanDeleteView,
    LoanUpdateView,
)


class DetailLoanView:
    pass


urlpatterns = [
    path("", LoanListView.as_view(), name="loan_list"),
    path("create/", LoanCreateView.as_view(), name="loan_create"),
    path("<int:pk>/get/", LoanDetailView.as_view(), name="loan_detail"),
    path("<int:pk>/delete/", LoanDeleteView.as_view(), name="loan_delete"),
    path("<int:pk>/edit/", LoanUpdateView.as_view(), name="loan_edit"),
]
