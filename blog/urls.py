from django.urls import path

from blog.views import ServiceListView, ServiceDetailView, CasesListView, PostListView, PostDetailView

urlpatterns = [
    path('services', ServiceListView.as_view()),
    path('service/<int:service_id', ServiceDetailView.as_view()),
    path('cases', CasesListView.as_view()),
    path('list', PostListView.as_view()),
    path('<str:slug>', PostDetailView.as_view())
]