#from django.conf.urls import url
from .views import line_chart, line_chart_json
from django.urls import  path


urlpatterns = [
  #'...',
  path('', line_chart, name='line_chart'),
  path('chart', line_chart, name='line_chart'),
  path('chartJSON', line_chart_json, name='line_chart_json'),
]
