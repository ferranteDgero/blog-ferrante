from django.urls import path
from .views import HomeView, about, PageListView, PageDetailView, PageCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
]