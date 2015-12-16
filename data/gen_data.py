from __future__ import division
import pandas as pd
import datetime

def to_aqi(pm25):
	for i in range(len(pm25_cutoffs)-1):
		if pm25>=pm25_cutoffs[i] and pm25<pm25_cutoffs[i+1]:
			return (((aqi_cutoffs[i+1] - aqi_cutoffs[i])/(pm25_cutoffs[i+1] - pm25_cutoffs[i]))*(pm25 - pm25_cutoffs[i])) + aqi_cutoffs[i]
	if pm25>250:
		aqi = (((400-300)/(250-120))*(pm25-250))+400
		if aqi>500:
			aqi=500
		return aqi	

df = pd.read_csv('readings_12042015.csv',dtype={'concentration':object})
df.dtypes
df = df.loc[(df.station_name=="R K Puram") | (df.station_name=="Anand Vihar") | (df.station_name=="IGI Airport") | (df.station_name=="Mandir Marg") | (df.station_name=="Civil Lines") | (df.station_name=="Punjabi Bagh")]

df = df.convert_objects(convert_numeric=True)

# take the simple daily average
df = df.loc[df.parameter_name=='PM2.5']
df['pm25'] = df.concentration
df = df.drop(['parameter_name','concentration'],1)
df = df.loc[df.pm25>0]

df_grouped = df[['station_name','date','pm25']].groupby(['station_name','date']).mean().reset_index()

df_grouped['datetime'] = pd.to_datetime(df_grouped.date,format='%d/%m/%Y')
df_grouped = df_grouped.loc[df_grouped.datetime >= datetime.datetime(2015,7,1)]

aqi_cutoffs = [0,50,100,200,300,400,500]
pm25_cutoffs = [0,30,60,90,120,250]

df_grouped['pm25_aqi'] = df_grouped['pm25'].apply(lambda x: to_aqi(x))

df_grouped = df_grouped.sort(['station_name','datetime'])
df_grouped = df_grouped.drop('datetime',1)
print df_grouped

df_grouped.to_csv('daily_pm25_new.csv',index=False)
