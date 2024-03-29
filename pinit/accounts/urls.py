from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register/',views.user_register, name='user_register'),
    path('<str:username>/profile', views.profile, name='profile'),
    path('<str:username>/profile/saved/', views.profile,name='profile_saved'),
    path('settings/edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/',views.user_logout,name='user_logout'),
    path('settings/delete-account/', views.delete_account_view, name='delete_account_view'),
    path('settings/delete-account/delete/', views.delete_account, name='delete_account'),
    path('profile/follow/<str:id>',views.follow_user,name='follow_user'),
    path('profile/unfollow/<str:id>',views.unfollow_user,name='unfollow_user'),
]