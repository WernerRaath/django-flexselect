from django.conf.urls import include, url
from flexselect import views as flex_views

urlpatterns = [
	url(r'^field_changed/?', flex_views.field_changed, name='field_changed')
]
