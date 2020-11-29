from rest_framework import serializers
from ml_api.models import FileUpload,BestModel


class DataSerializer(serializers.ModelSerializer):
	class Meta:
		model = FileUpload
		fields = '__all__'

class BestModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = BestModel
		fields = '__all__'