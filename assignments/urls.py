from django.conf.urls import url
from assignments import views


urlpatterns = [
    url(r'^assignments/new$', views.NewView.as_view(), name='assignment-new'),
    url(r'^assignments/(?P<pk>[0-9]+)/$', views.ShowView.as_view(), name='assignment-show'),
    url(r'^$', views.IndexView.as_view()),
]
