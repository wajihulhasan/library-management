"""
URL configuration for libraryManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Books-related paths
    path("books/", include("books.urls")),
    path("books/reviews/", include("bookReviews.urls")),
    path("books/copies/", include("bookCopies.urls")),
    path("books/orders/", include("bookOrders.urls")),
    path("books/fines/", include("fines.urls")),
    path("books/genres/", include("genres.urls")),
    path("books/inventory-requests/", include("inventoryRequests.urls")),
    path("books/loans/", include("loans.urls")),
    path("books/publishers/", include("publishers.urls")),
    path("books/suppliers/", include("supplier.urls")),

    # Authors-related paths
    path("authors/", include("authors.urls")),

    # Employees-related paths
    path("employees/", include("employees.urls")),
    path("employees/positions/", include("positions.urls")),

    # Departments-related paths
    path("departments/", include("departments.urls")),

    # Events-related paths
    path("events/", include("events.urls")),
    path("events/locations/", include("locations.urls")),
    path("events/registrations/", include("eventRegistration.urls")),
    path("events/reservations/", include("reservations.urls")),

    # Miscellaneous paths
    path("notifications/", include("notifications.urls")),
    path("patrons/", include("patrons.urls")),
    path("staff-schedules/", include("staffSchedules.urls")),
    path("user-logs/", include("userLogs.urls")),
]
