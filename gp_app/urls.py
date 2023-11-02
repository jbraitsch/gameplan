from django.urls import path
from . import views

urlpatterns = [
 #path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('business/<int:pk>', views.BusinessDetailView.as_view(), name='business-detail'),
    path('business/create_business/', views.createBusiness, name='create_business'),
    path('business/<int:business_id>/delete_business/',views.deleteBusiness, name='delete_business' ),
    path('business/<int:business_id>/update_business/', views.updateBusiness, name='update_business' ),
    ]
