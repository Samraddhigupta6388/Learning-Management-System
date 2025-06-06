from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home,name='home'),
    path('layout',views.layout,name='layout'),
    path('homelogin/',views.user_login,name='homelogin'),
    path('services',views.services,name='services'),
    path('courses',views.courses,name='courses'),
    path('contact',views.contact,name='contact'),
    # path('study',views.study,name='study'),
    path('Regi',views.Regi,name='Regi'),
    path('about',views.about,name='about'),
    path('save',views.save_view,name='save'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('logcode',views.logcode,name='logcode'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentlayout',views.studentlayout,name='studentlayout'),
    path('adminlayout',views.adminlayout,name='adminlayout'),
    path('showdata',views.manageuser,name='showdata'),
    path('uploadstudy',views.uploadstudy,name='uploadstudy'),
    path('uploadassignments',views.uploadassignments,name='uploadassignments'),
    path('uploadlecture',views.uploadlecture,name='uploadlecture'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('viewstudy',views.viewstudy,name='viewstudy'),
    path('viewassignment',views.viewassignment,name='viewassignment'),
    path('viewlecture',views.viewlecture,name='viewlecture'),
    path('complaint',views.complaint,name='complaint'),
    path('feedback',views.feedback,name='feedback'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('viewcomplaint',views.viewcomplaint,name='viewcomplaint'),
    path('notification',views.notification,name='notification'),
    path('UsmSave',views.usmsave,name='Usmsave'),
    path('assisave',views.assisave,name='assisave'),
    path('lecturesave',views.lecturesave,name='lecturesave'),
    path('Complaintsave/<int:id>',views.Complaintsave,name='Complaintsave'),
    path('Feedbacksave/<int:id>',views.Feedbacksave,name='Feedbacksave'),
    path('enqsave',views.enqsave,name='enqsave'),
    path('notisave',views.notisave,name='notisave'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    path('deleteUsm/<int:id>',views.deleteUsm,name='deleteUsm'),
    path('deletelect/<int:id>',views.deletelect,name='deletelect'),
    path('deleteassi/<int:id>',views.deleteassi,name='deleteassi'),
    path('updatedata/<int:id>',views.updatedata,name='updatedata'),
    path('updateform',views.updateform,name='updateform'),
    path('logout',views.logout,name='logout'),
    path('updatepro',views.updatepro,name='updatepro'),
    path('upsave',views.upsave,name='upsave'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)