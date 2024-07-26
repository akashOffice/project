from django.urls import path
from api import views

urlpatterns = [
    path('',views.test),
    path('get/',views.getPerson),
    path('getone/',views.getOne),
    path('add',views.add),
    path('update',views.update),
    path('delete',views.delete),
    path('mail',views.mailtest)
]