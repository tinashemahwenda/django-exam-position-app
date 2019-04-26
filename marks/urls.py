from django.urls import path
from . import views
urlpatterns = [
    path('', views.table,name='marks-table'),

]