
from django.urls import path
from . import views

urlpatterns = [
 path('',views.home,name='home'),
 path('add-patient/',views.add_patient),
 path('patients/',views.patients,name='patients'),
 path('update/<int:id>/',views.update_patient),
 path('delete/<int:id>/',views.delete_patient),
 path('add-doctor/',views.add_doctor),
 path('doctors/',views.doctors),
 path('add-appointment/',views.add_appointment),
]
