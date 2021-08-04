"""

Developed By : sumit kumar
facebook : fb.com/sumit.luv
Youtube :youtube.com/lazycoders


"""

from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView, LogoutView

# -------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    path('adminclick', views.adminclick_view),
    path('consumerclick', views.consumerclick_view),
    path('farmerclick', views.farmerclick_view),

    path('adminsignup', views.admin_signup_view),
    path('consumersignup', views.consumer_signup_view, name='consumersignup'),
    path('farmersignup', views.farmer_signup_view),

    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('consumerlogin', LoginView.as_view(template_name='hospital/consumerlogin.html')),
    path('farmerlogin', LoginView.as_view(template_name='hospital/farmerlogin.html')),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'), name='logout'),

    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-consumer', views.admin_consumer_view, name='admin-consumer'),
    path('admin-view-consumer', views.admin_view_consumer_view, name='admin-view-consumer'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,
         name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view, name='update-doctor'),
    path('admin-add-consumer', views.admin_add_consumer_view, name='admin-add-consumer'),
    path('admin-approve-consumer', views.admin_approve_consumer_view, name='admin-approve-consumer'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view, name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view, name='reject-doctor'),
    path('admin-view-consumer-specialisation', views.admin_view_consumer_specialisation_view,
         name='admin-view-consumer-specialisation'),

    path('admin-farmer', views.admin_farmer_view, name='admin-farmer'),
    path('admin-view-farmer', views.admin_view_farmer_view, name='admin-view-farmer'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,
         name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view, name='update-patient'),
    path('admin-add-farmer', views.admin_add_farmer_view, name='admin-add-farmer'),
    path('admin-approve-farmer', views.admin_approve_farmer_view, name='admin-approve-farmer'),
    path('approve-patient/<int:pk>', views.approve_patient_view, name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view, name='reject-patient'),
    path('admin-discharge-farmer', views.admin_discharge_farmer_view, name='admin-discharge-farmer'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view, name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view, name='download-pdf'),

    path('admin-booking', views.admin_booking_view, name='admin-booking'),
    path('admin-view-appointment', views.admin_view_appointment_view, name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view, name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view, name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view, name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view, name='reject-appointment'),
]

# ---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns += [
    path('doctor-dashboard', views.doctor_dashboard_view, name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view, name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view, name='doctor-view-patient'),
    path('doctor-view-discharge-patient', views.doctor_view_discharge_patient_view,
         name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view, name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view, name='doctor-view-appointment'),
    path('doctor-delete-appointment', views.doctor_delete_appointment_view, name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view, name='delete-appointment'),
]

# ---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns += [

    path('patient-dashboard', views.patient_dashboard_view, name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view, name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view, name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view, name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view, name='patient-discharge'),

]
