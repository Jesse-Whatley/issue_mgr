from django.urls import path
from issues import views


urlpatterns = [
    path("", views.BoardView.as_view(), name="board"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.StatusUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.IssueDeleteView.as_view(), name="delete"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
]