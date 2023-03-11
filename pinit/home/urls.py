from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('download/<str:filename>',views.download,name="download"),
    path('save/<int:pin_id>',views.save_pin_profile,name="save-pin"),
    path('search/',views.search_pins,name="search-pins"),
]