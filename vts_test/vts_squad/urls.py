from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<pre_page>\d+)&(?P<next_page>\d+)$', views.index, name='index'),
    url('^submit/$', views.job_submit, name='submit'),
    url('^resubmit/$', views.job_resubmit, name='resubmit'),
    # url('^job_info/$', views.job_info, name='job_info'),
    url('^job_info/(?P<jid>\d+)/$', views.job_info_detail, name='job_info_detail'),
    url('^my_submit/$', views.my_submit, name='my_submit'),
    url('^my_comment/$', views.my_comment, name='my_comment'),
    url('^get_vts_log_path/$', views.get_vts_log, name='get_vts_log'),
    url('^get_pac_nodes/', views.get_pac_nodes, name='get_pac_nodes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)