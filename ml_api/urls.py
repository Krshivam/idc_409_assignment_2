from django.urls import path
from ml_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('',views.HomePage),
	path('accuracy/',views.accuracy),
	path('upload/',views.UploadedFilesList.as_view()),
	path('model/',views.BestModelList.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)