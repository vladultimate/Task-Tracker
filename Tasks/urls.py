from django.urls import path
from .views import BoardListView, BoardDetailView, BoardCreateView, BoardEditView, BoardDeleteView, LoginView, RegisterView

urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('board/create/', BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/edit/', BoardEditView.as_view(), name='board_edit'),
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='board_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')

]
