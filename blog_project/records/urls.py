from django.conf.urls import url, include
from records import views

urlpatterns = [
	url(r'^$', views.PostListView.as_view(), name='list_posts'),
	url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail_post'),
	url(r'^(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='update_post'),
	url(r'^(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='delete_post'),
	url(r'^create/$', views.PostCreate.as_view(), name='create_posts'),


]