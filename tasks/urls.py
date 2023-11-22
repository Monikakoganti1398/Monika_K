
from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insert',views.insertData,name="insertData"),
    path('create',views.create,name="create"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
]
