import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    'indo_12_1.xls', 
    header = 3, 
    names = ['provinsi/tahun', 1971, 1980, 1990, 1995, 2000, 2010],
    na_values = ['-', 'NaN']
)
df = df.interpolate()
df = df.drop([34,35])       #drop baris catatan dan sumber
# df = df.set_index('provinsi')
df.set_index('provinsi/tahun',inplace=True)
dfSensus = df.transpose()
print(dfSensus)

from sklearn import linear_model
model = linear_model.LinearRegression()

model.fit(dfSensus[['provinsi/tahun']], dfSensus.loc[dfSensus['Jawa Barat'].max()])

print(model.coef_)

print(model.intercept_)

# #Plot Best Fit Line
# plt.plot(df[''])