from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include


app_name='orange'


urlpatterns= [
    path('',views.Homepage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('thanks',views.ThanksPage.as_view(),name='thanks'),
    path('signin',views.Signin.as_view(),name='signin'),
    path('welcome',views.Welcomepage.as_view(),name='welcome'),
    path('calander',views.Calander.as_view(),name='calander'),
    path('newevent',views.NewEvent.as_view(),name='newevent'),
    path('saveday',views.SaveDay.as_view(),name='saveday'),
    path('profile',views.Profile.as_view(),name='profile'),
    path('neworg',views.NewOrg.as_view(),name='neworg'),
    path('sendinfo',views.SendInfo.as_view(),name='sendinfo'),
    path('sendemail',views.SendEmail.as_view(),name='sendemail'),
    path('emailtemplate',views.EmailTemplate.as_view(),name='emailtemplate'),
    path('about',views.Aboutpage.as_view(),name='about'),
    path('goal',views.Goalpage.as_view(),name='goal'),
    re_path(r'org/(?P<slug>[-\w]+)/$',views.OrganizationInfo.as_view(),name='orginfo'),
    re_path(r'user/(?P<slug>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.UserPage.as_view(),name='user'),
    re_path(r'(?P<slug>[-\w]+)/$',views.EventInfo.as_view(),name='eventinfo'),
    ]
