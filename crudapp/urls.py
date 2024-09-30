from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_view, name="test_view"),
    path('', views.note_list, name='note_list'),  
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:note_id>/edit/', views.note_update, name='note_update'),
    path('note/<int:note_id>/delete/', views.note_delete, name='note_delete'),
    path('note/<int:note_id>/check-off/', views.note_check_off, name='note_check_off'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("logout", views.logout_view, name="logout"),
]
