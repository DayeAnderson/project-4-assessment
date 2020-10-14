from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hunters/', views.hunters_index, name='index'),
  path('hunters/<int:hunter_id>/', views.hunters_detail, name='detail'),
  path('hunters/create/', views.HunterCreate.as_view(), name='hunters_create'),
  path('hunters/<int:pk>/update/', views.HunterUpdate.as_view(), name='hunters_update'),
  path('hunters/<int:pk>/delete/', views.HunterDelete.as_view(), name='hunters_delete'),
  path('weapons/', views.WeaponList.as_view(), name='weapons_index'),
  path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapons_detail'),
  path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
  path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
  path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
  path('hunters/<int:hunter_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),
  path('accounts/signup/', views.signup, name='signup'),
  path('hunters/<int:hunter_id>/add_photo/', views.add_photo, name='add_photo'),

]