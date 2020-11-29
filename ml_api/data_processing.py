import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from django.conf import settings
# Read
def preprocess():
	df = pd.read_csv(os.path.join(settings.MEDIA_ROOT,'mediafiles','insurance.csv'))
	df.dropna(inplace=True)


	#Quantify

	le_1 = preprocessing.LabelEncoder()
	le_1.fit(df['Vehicle_Age'])
	Vehicle_Age_quant = le_1.transform(df['Vehicle_Age'])
	le_2 = preprocessing.LabelEncoder()
	le_2.fit(df['Vehicle_Damage'])
	Vehicle_Damage_quant = le_2.transform(df['Vehicle_Damage'])
	df['Vehicle_Age_quant'] = Vehicle_Age_quant
	df['Vehicle_Damage_quant'] = Vehicle_Damage_quant

	#get Relevant columns

	df2 = pd.DataFrame(df,columns=['Age','Driving_License','Region_Code','Previously_Insured','Annual_Premium','Policy_Sales_Channel','Vintage','Vehicle_Age_quant','Vehicle_Damage_quant','Response'])

	# Normalization
	scaler = MinMaxScaler()
	y = df2['Response']
	data = df2.drop(['Response'],axis=1)
	data[data.columns] = scaler.fit_transform(data[data.columns])
	return data,y


