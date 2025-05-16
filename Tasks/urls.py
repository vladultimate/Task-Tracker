from django.urls import path
from .views import BoardListView, BoardDetailView, BoardCreateView

urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('board/create/', BoardCreateView.as_view(), name='board_create'),
]
