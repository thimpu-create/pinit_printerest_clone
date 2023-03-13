from django.urls import path
from . import views
app_name = 'pins'
urlpatterns = [
    path('create/',views.create_pin,name = 'create_pin'),
    path('pin/<int:id>/', views.pin_detail, name='pin_detail'),
    path('follow/<str:id>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:id>/', views.unfollow_user, name='unfollow_user'),
    path('comment/<str:id>/', views.add_comment, name='add_comment'),

]