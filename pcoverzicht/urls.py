from django.conf.urls import url
from support import views

from pcoverzicht.views import ComputerCreate, ComputerDelete, ComputerListView, ComputerUpdate, \
                                 SoftwareCreate, SoftwareDelete, SoftwareListView, SoftwareUpdate, ComputerForm

urlpatterns = [
        url(r'^computer/list/$',                ComputerListView.as_view(),     name='computer_list'),
        url(r'^computer/delete/(?P<pk>\d+)$',   ComputerDelete.as_view(),       name='computer_delete'),
        url(r'^computer/new$',                  ComputerCreate.as_view(),       name='computer_new'),
        url(r'^computer/update/(?P<pk>\d+)$',   ComputerUpdate.as_view(),       name='computer_update'),
        url(r'^computer/form/(?P<pk>\d+)$',   ComputerForm.as_view(),         name='computer_form'),
        url(r'^software/list/$',                SoftwareListView.as_view(),     name='software_list'),
        url(r'^software/update/(?P<pk>\d+)$',   SoftwareUpdate.as_view(),       name='software_update'),
        url(r'^software/new$',                  SoftwareCreate.as_view(),       name='software_new'),
        url(r'^software/delete/(?P<pk>\d+)$',   SoftwareDelete.as_view(),       name='software_delete'),
        ]
