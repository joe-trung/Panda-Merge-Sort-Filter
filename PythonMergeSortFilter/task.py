import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

df_temp = pd.read_csv('tempYearly.csv')
df_rain = pd.read_csv('rainYearly.csv')

# print(df_temp)
# print(df_rain)

df_temp_filter = df_temp.query('Temperature <40 & Temperature>0')
# print(df_temp_filter)

# df_temp_filter.plot.scatter(x='Year', y='Temperature', label='Temperature in Years')
# plt.show()


df_rain_filter = df_rain.query('Rainfall <6 & Rainfall > 0')
# print(df_rain_filter)

# df_rain_filter.plot.scatter(x='Year', y='Rainfall', label='Rain in Years')
# plt.show()

# df_merge = pd.merge(df_temp_filter, df_rain_filter, on='Year', how='outer')  ###THERE WILL BE SOME NAN
df_merge = pd.merge(df_temp_filter, df_rain_filter, on='Year', how='inner')
# print(df_merge)

df_temp_sort = df_merge.sort_values(by='Temperature')
# print(df_temp_sort)


df_rain_sort = df_merge.sort_values(by='Rainfall', ascending=False)
# print(df_rain_sort)

# sns.set(rc={'figure.figsize':(12, 6)})
# sns.jointplot(data=df_merge, kind='reg', x='Rainfall', y='Temperature', )
# # reg: regression line
# plt.show()