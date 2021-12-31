from django.urls import path

from . import views

app_name = 'commissions'
urlpatterns = [
    path('', views.index, name='index'),
    path('tos/', views.tos, name='tos'),
    path('commission/', views.commission, name='commission'),
    path('account/', views.account, name='account'),
    path('commission/<int:id>/', views.view_comm, name='commreq'),
#     todo need to figure out accounts and authentication stuff
#     then can make commission_request page
]