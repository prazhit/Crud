from django.urls import path
from . import views

urlpatterns = [
    path('add',views.add_user, name='add_user'),
    path('show',views.show_user, name='show_user'),
    path('',views.show_user, name='show_user'),
    path('edit/<int:id>',views.edit_user, name='edit_user'),
    path('delete/<int:id>',views.delete, name='delete_user')
]