
from django.contrib import admin
from django.urls import path
from home import views as home_views
from adm import views as adm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.hm),
    path('reg/', home_views.registration),
    path('result/', home_views.rs),
    path('payment/', home_views.pay),
    path('contact/', home_views.contactView),
    path('notice/', home_views.noti),
    path('land/', home_views.land),
    path('teacher/', adm_views.ah),
    path('noticelist/', adm_views.NoticeList),
    path('userinfo/', adm_views.Rinfo),
    path('noticelist/info/<str:action>/<str:id>', adm_views.action_handler),
    path('userinfo/info/<str:action>/<str:id>', adm_views.act_handler),
    path('newnotice/', adm_views.newNotice),
]
