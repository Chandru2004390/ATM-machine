from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('add_del',views.add_del,name='add_del'),
    path('add',views.add,name='add'),
    path('dell',views.dell,name='dell'),
    path('tab',views.tab,name='tab'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('add_details',views.add_details,name='add_details'),
    path('depo',views.depo,name='depo'),
    path('damount',views.damount,name='damount'),
    path('wamount',views.wamount,name='wamount'),
    path('wepo',views.wepo,name='wepo'),
    path('bal',views.bal,name='bal'),
    path('pc',views.pc,name='pc'),
    path('pinc',views.pinc,name='pinc'),
    path('pasc',views.pasc,name='pasc'),
    path('chpinpin',views.chpinpin,name='chpinpin'),
    path('chpaspin',views.chpaspin,name='chpaspin'),
    path('chotppin',views.chotppin,name='chotppin'),
    path('chpaspas',views.chpaspas,name='chpaspas'),
    path('chpinpas',views.chpinpas,name='chpinpas'),
    path('chotppas',views.chotppas,name='chotppas'),
]