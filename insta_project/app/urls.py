from django.urls import path
form . import views

urlpatterns = [
    path('view/', views.view, name = 'view'),
    path('delete/<int:post_id>', views.deleting, name = 'delete_post')
]