from django.contrib import admin
from django.urls import path,include
#from userapp import views as main_views
# from . import views
from .views import AssignmentCreateView
from .views import AssignmentTrackerCreateView

urlpatterns = [
    path('create_assignment/', AssignmentCreateView.as_view(), name='create_assignment'),
    path('assign_assignment/', AssignmentTrackerCreateView.as_view(), name='assign_assignment'),
]
