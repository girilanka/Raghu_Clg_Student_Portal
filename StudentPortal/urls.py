"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home , name='home'),
    
    path('college_all_students/',views.college_all_students , name='college_all_students'),
    
    path('csm_1st_years/',views.csm_1st_years , name='csm_1st_years'),
    path('csm_2nd_years/',views.csm_2nd_years , name='csm_2nd_years'),
    path('csm_3rd_years/',views.csm_3rd_years , name='csm_3rd_years'),
    path('csm_4th_years/',views.csm_4th_years , name='csm_4th_years'),
    
    path('csd_1st_years/',views.csd_1st_years , name='csd_1st_years'),
    path('csd_2nd_years/',views.csd_2nd_years , name='csd_2nd_years'),
    path('csd_3rd_years/',views.csd_3rd_years , name='csd_3rd_years'),
    path('csd_4th_years/',views.csd_4th_years , name='csd_4th_years'),
    
    path('csc_1st_years/',views.csc_1st_years , name='csc_1st_years'),
    path('csc_2nd_years/',views.csc_2nd_years , name='csc_2nd_years'),
    path('csc_3rd_years/',views.csc_3rd_years , name='csc_3rd_years'),
    path('csc_4th_years/',views.csc_4th_years , name='csc_4th_years'),
    
    path('cse_1st_years/',views.cse_1st_years , name='cse_1st_years'),
    path('cse_2nd_years/',views.cse_2nd_years , name='cse_2nd_years'),
    path('cse_3rd_years/',views.cse_3rd_years , name='cse_3rd_years'),
    path('cse_4th_years/',views.cse_4th_years , name='cse_4th_years'),
    
    path('mech_1st_years/',views.mech_1st_years , name='mech_1st_years'),
    path('mech_2nd_years/',views.mech_2nd_years , name='mech_2nd_years'),
    path('mech_3rd_years/',views.mech_3rd_years , name='mech_3rd_years'),
    path('mech_4th_years/',views.mech_4th_years , name='mech_4th_years'),
    
    path('civil_1st_years/',views.civil_1st_years , name='civil_1st_years'),
    path('civil_2nd_years/',views.civil_2nd_years , name='civil_2nd_years'),
    path('civil_3rd_years/',views.civil_3rd_years , name='civil_3rd_years'),
    path('civil_4th_years/',views.civil_4th_years , name='civil_4th_years'),
    
    path('ece_1st_years/',views.ece_1st_years , name='ece_1st_years'),
    path('ece_2nd_years/',views.ece_2nd_years , name='ece_2nd_years'),
    path('ece_3rd_years/',views.ece_3rd_years , name='ece_3rd_years'),
    path('ece_4th_years/',views.ece_4th_years , name='ece_4th_years'),
    
    path('eee_1st_years/',views.eee_1st_years , name='eee_1st_years'),
    path('eee_2nd_years/',views.eee_2nd_years , name='eee_2nd_years'),
    path('eee_3rd_years/',views.eee_3rd_years , name='eee_3rd_years'),
    path('eee_4th_years/',views.eee_4th_years , name='eee_4th_years'),
    
    path('search/', views.search ,name = 'search'),
    
    path('students/', include('students.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
