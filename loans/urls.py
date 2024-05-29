from django.urls import path
from .views import LoanListView, LoanDetailView, CreateLoanView, DeleteLoanView, UpdateLoanView

urlpatterns = [
    path("", LoanListView.as_view(), name="loan_list"),
    path("create/", CreateLoanView.as_view(), name="loan_create"),
    path("<int:pk>/get/", LoanDetailView.as_view(), name="loan_detail"),
    path("<int:pk>/delete/", DeleteLoanView.as_view(), name="loan_delete"),
    path("<int:pk>/edit/", UpdateLoanView.as_view(), name="loan_edit")
]
