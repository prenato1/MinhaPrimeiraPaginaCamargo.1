from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('page/create/', PageCreateView.as_view(), name='page_create'),
    path('page/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('page/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]
