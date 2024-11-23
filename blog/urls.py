from django.urls import path

from blog.views import ServiceListView, ServiceDetailView, CasesListView, PostListView, PostDetailView, \
    ServicePricesListView, AdvantageListView, FloorWorksListView, QuestionCreateView

urlpatterns = [
    path('services/', ServiceListView.as_view()),
    path('service/<str:slug>/', ServiceDetailView.as_view()),
    path('question/', QuestionCreateView.as_view()),
    path('cases/', CasesListView.as_view()),
    path('list/', PostListView.as_view()),
    path('services/prices/', ServicePricesListView.as_view()),
    path('floor_works/', FloorWorksListView.as_view()),
    path('advantage/', AdvantageListView.as_view()),
    path('<str:slug>/', PostDetailView.as_view()),
]