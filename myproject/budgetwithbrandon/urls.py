from django.urls import path
from .views import TransactionListCreate, TransactionDetail, TimelineListCreate, TimelineDetail
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, TimelineViewSext


urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
     path('timelines/', TimelineListCreate.as_view(), name='timeline-list'),
    path('timelines/<int:pk>/', TimelineDetail.as_view(), name='timeline-detail'),
        
]
