from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # ----------employee-------------

    path('',views.index),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('about/',views.about),
    # path('login/',views.login),
    path('single/',views.single),
    path('register1/',views.adregisterform1),
    path('home/',views.home),
    path('empregister/',views.empregister),
    path('emp_login_form/',views.emp_login_form),
    path('regform1/',views.regform1),


    # --------ADMIN----------

    # path('registration/',views.registration),
    path('basic_table/',views.basic_table),
    path('index2/',views.index2),
    path('ad_login_form/',views.ad_login_form),
    path('logout/',views.logout1),
    path('userdelete/',views.userdelete),
    path('userupdate/',views.userupdate),

# reg details view , update and delete

    path('emp_reg_view1/',views.emp_reg_view1),
    path('userdelete2/',views.userdelete2),
    path('userupdate2/',views.userupdate2),





    




]
