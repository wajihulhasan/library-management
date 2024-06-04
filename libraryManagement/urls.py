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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from libraryManagement.views import landing_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing_page, name="landing"),
    # Books-related paths
    path("books/", include(("books.urls", "books"), namespace="books")),
    path(
        "books/reviews/",
        include(("bookReviews.urls", "bookReviews"), namespace="bookReviews"),
    ),
    path(
        "books/copies/",
        include(("bookCopies.urls", "bookCopies"), namespace="bookCopies"),
    ),
    path(
        "books/orders/",
        include(("bookOrders.urls", "bookOrders"), namespace="bookOrders"),
    ),
    path("books/fines/", include(("fines.urls", "fines"), namespace="fines")),
    path("books/genres/", include(("genres.urls", "genres"), namespace="genres")),
    path(
        "books/inventory-requests/",
        include(
            ("inventoryRequests.urls", "inventoryRequests"),
            namespace="inventoryRequests",
        ),
    ),
    path("books/loans/", include(("loans.urls", "loans"), namespace="loans")),
    path(
        "books/publishers/",
        include(("publishers.urls", "publishers"), namespace="publishers"),
    ),
    path(
        "books/suppliers/", include(("supplier.urls", "supplier"), namespace="supplier")
    ),
    # Authors-related paths
    path("authors/", include(("authors.urls", "authors"), namespace="authors")),
    # Employees-related paths
    path("employees/", include(("employees.urls", "employees"), namespace="employees")),
    path(
        "employees/positions/",
        include(("positions.urls", "positions"), namespace="positions"),
    ),
    # Departments-related paths
    path(
        "departments/",
        include(("departments.urls", "departments"), namespace="departments"),
    ),
    # Events-related paths
    path("events/", include(("events.urls", "events"), namespace="events")),
    path(
        "events/locations/",
        include(("locations.urls", "locations"), namespace="locations"),
    ),
    path(
        "events/registrations/",
        include(
            ("eventRegistration.urls", "eventRegistration"),
            namespace="eventRegistration",
        ),
    ),
    path(
        "events/reservations/",
        include(("reservations.urls", "reservations"), namespace="reservations"),
    ),
    # Miscellaneous paths
    path(
        "notifications/",
        include(("notifications.urls", "notifications"), namespace="notifications"),
    ),
    path("patrons/", include(("patrons.urls", "patrons"), namespace="patrons")),
    path(
        "staff-schedules/",
        include(("staffSchedules.urls", "staffSchedules"), namespace="staffSchedules"),
    ),
    path("user-logs/", include(("userLogs.urls", "userLogs"), namespace="userLogs")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)