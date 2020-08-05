from django.urls import path
from . import views

urlpatterns = [
    path('', views.allshows),
    path('new', views.showsnew),
    path('create', views.createshow),
    path('<int:show_id>/edit', views.editshow),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>/', views.tvshow),
    path('<int:show_id>/delete', views.delete),
]