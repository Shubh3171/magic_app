from django.contrib import admin
from django.urls import path
from website import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name= "Home"),
    path("about/", views.about, name= "About"),
    path("services/", views.services, name= "Serices"),
    path("contact/", views.contact, name= "Contact"),
    path("styling/", views.styling, name= "styling"),
    path("save_styling/", views.save_styling, name= "save_styling"),
    path("prototype/", views.prototype, name= "Prototype"),
    path("design/", views.design, name= "Design"),
    path("cae/",views.cae , name="CAE"),
    path("save_design/", views.save_design, name= "save_design"),
    path("save_prototype/", views.save_prototype, name= "save_prototype"),
    path("save_cae/", views.save_cae, name= "save_cae")
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )