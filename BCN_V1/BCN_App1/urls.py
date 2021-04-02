from django.urls import path
from BCN_App1.views import post_edit
from BCN_App1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student_fees, name='add_student_fees'),
    path('transactions/', views.fees_transactions, name='fees_transactions'),
    path('details/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('alldetail/', views.alldetail, name='alldetail'),
    path('BCN_V1/edit/<int:pk>/', post_edit, name='post_edit'),
    path('fees_transaction/', views.fees_data, name='feesdata'),
    path('BCN_V1/fees/<int:pk>/', views.fees_up, name='fees_up'),
    path('check_st_name/', views.st_name, name='st_name'),
    path('BCN_V1/update/<int:pk>/', views.update_data, name='update_data'),
]
