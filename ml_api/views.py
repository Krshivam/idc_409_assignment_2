from django.shortcuts import render
from ml_api.serializers import DataSerializer,BestModelSerializer
from ml_api.models import FileUpload,BestModel
from rest_framework import generics
from django.http import HttpResponse
from ml_api import data_processing
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd

# Create your views here.


def HomePage(request):
	return HttpResponse('Welcome to HomePage.Enpoints are upload,model,accuracy')

def accuracy(request):
	X_test,y_test = data_processing.preprocess()
	model = pickle.load(open('C:\\cbase\\ml_site\\media\\mediafiles\\gbdt.sav','rb'))
	score = model.score(X_test, y_test)
	return HttpResponse('Accuracy is '+ str(int(score*100)) + '% and model is gradient boosted decision tree')

class UploadedFilesList(generics.ListCreateAPIView):
	serializer_class = DataSerializer
	def perform_create(self,serializer):
		serializer.save()
	def get_queryset(self):
		return FileUpload.objects.all()

class BestModelList(generics.ListCreateAPIView):
	serializer_class = BestModelSerializer
	def perform_create(self,serializer):
		serializer.save()
	def get_queryset(self):
		return BestModel.objects.all()
