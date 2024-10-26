from django.urls import path

from blog.views import ServiceListView, ServiceDetailView

urlpatterns = [
    path('services', ServiceListView.as_view()),
    path('service/<int:service_id', ServiceDetailView.as_view())
]