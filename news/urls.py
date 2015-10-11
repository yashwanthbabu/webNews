from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^ndtv_news/', views.headnews, name="head_line_news"),
    url(r'^cnn_news/', views.cnnheadlinenews, name="cnn_head_line_news"),
    url(r'^zee_news/', views.zeeheadlinenewes, name="zee_head_line_news"),

)
