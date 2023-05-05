from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create/',views.create_board,name='create_board'),
    path('<str:username>/<str:board_name>/', views.board_detail, name='board_detail'),
]