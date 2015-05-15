from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from pbpk import views

urlpatterns = patterns('',
    url(r'^$', views.WelcomePage, name='home'),
    url(r'^default', views.DefaultModel),
    #url(r'^oldModel', login_required(views.OldModels)),
    #url(r'^editDrug', login_required(views.EditDrug)),
    url(r'^editIntermediate', login_required(views.EditIntermediate)),
    url(r'^edit_model', login_required(views.Edit)),
    url(r'^NewModel', login_required(views.InitPage)),
    url(r'^DeleteModel', login_required(views.delete)),
    url(r'^userprofile', login_required(views.user_profile)),
    #url(r'^tutorial_edit', views.tutorial_edit),
    url(r'^tutorial', views.tutorial),
    #url(r'^mpc_input?', views.MPCInput),
    #url(r'^results', views.MPCResults),

    # Authentication module
    url(r'^accounts/', include('allauth.urls')),

    # Administration page
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ajax_color_request/$', views.ajax_color_request),


)
