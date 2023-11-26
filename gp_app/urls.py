from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
 #path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name = 'register_page'),
    path('user/create_user', views.userPage, name = "create_user"),
    path('user/<int:pk>', views.UserView.as_view(), name="user_detail"),
    path('business/', views.BusinessListView.as_view(), name= 'business'),
    path('nhl/', views.listNHLTeams, name='nhl_teams_list'),
    path('nhl/<int:team_id>', views.NHLTeamDetails, name="nhl_team_details"),
    path('<str:city>/', views.indexCity, name='index_city'),
    path('business/<int:pk>', views.BusinessDetailView.as_view(), name='business-detail'),
    path('business/create_business/', views.createBusiness, name='create_business'),
    path('business/<int:business_id>/delete_business/',views.deleteBusiness, name='delete_business' ),
    path('business/<int:business_id>/update_business/', views.updateBusiness, name='update_business' ),
    
    ]
