from django.urls import path
from django.conf.urls.static import static

from hr import views

urlpatterns = [
    path("",views.login_view, name="login"),

    path("dashboard/",views.dashboard, name="dashboard"),
    path("logout/",views.logout_view, name="logout"),
    #path("viewemployees/", views.employees, name="viewemployees"),
    #employess related urls
    path("employees/",views.employee_list,name="employee_list"),
    path("employees/add/",views.employee_create,name="employee_create"),
    path("employees/<int:id>/edit/",views.employee_update,name="employee_update"),
    path("employees/<int:id>/delete/",views.employee_delete, name="employee_delete"),
    path("leave_approve/",views.leave_approve,name='leave_approve'),
    path("leave/<int:id>/action/",views.leave_action,name='leave_action'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/edit/<int:pk>/', views.department_update, name='department_update'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

    path('designations/', views.designation_list, name='designation_list'),
    path('designations/add/', views.designation_create, name='designation_create'),
    path('designations/edit/<int:pk>/', views.designation_update, name='designation_update'),
    path('designations/delete/<int:pk>/', views.designation_delete, name='designation_delete'),


]