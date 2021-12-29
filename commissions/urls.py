from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tos', views.tos, name='tos'),
    path('commission', views.commission, name='commission'),
#     path('account', views.account, name='account'),
#     todo need to figure out accounts and authentication stuff
#     then can make commission_request page
]