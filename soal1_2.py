import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================
# Preprocessing
# =========================================

df = pd.read_excel(
    'indo_12_1.xls',
    header = 3, 
    names = ['provinsi', 1971, 1980, 1990, 1995, 2000, 2010],
    na_values = ['-', 'NaN'],
)
df = df.dropna()
df = df.interpolate()
df = df.set_index('provinsi')

# =========================================
# Import Sklearn Linear Regression
# =========================================

from sklearn.linear_model import LinearRegression
model = LinearRegression()

# =========================================
# Plotting
# =========================================

plt.style.use('ggplot')

#Plot Provinsi Penduduk Terbanyak 2010
dfx = df.drop(df.tail(1).index)
dfprovmax2010 = dfx.loc[dfx.index[dfx[2010]==dfx[2010].max()]]
x = dfprovmax2010.columns.values
x1 = x.reshape(-1,1)
# print(x)
y1 = dfprovmax2010.values.reshape(6,)
model.fit(x1, y1)
pred1 = model.predict([[2050]])
plt.plot(x1, y1, 'g-', label = ''.join(dfprovmax2010.index.values))
plt.scatter(x1, y1, color = 'g')

#Plot Provinsi Penduduk Tesedikit 1971
dfprovmin1971 = df.loc[df.index[df[1971]==df[1971].min()]]
x = dfprovmin1971.columns.values
x2 = x.reshape(-1,1)
# print(x)
y2 = dfprovmin1971.values.reshape(6,)
model.fit(x2, y2)
pred2 = model.predict([[2050]])
plt.plot(x2, y2, 'b-', label = ''.join(dfprovmin1971.index.values))
plt.scatter(x2, y2, color = 'b')

#Plot Jumlah Penduduk Indonesia
dfsumcitizen = df.tail(1)
x = dfsumcitizen.columns.values
x3 = x.reshape(-1,1)
# print(x)
y3 = dfsumcitizen.values.reshape(6,)
model.fit(x3, y3)
pred3 = model.predict([[2050]])
plt.plot(x3, y3, 'r-', label = ''.join(dfsumcitizen.index.values))
plt.scatter(x3, y3, color = 'r')

#Plot Best Fit Line
model.fit(x1, y1)
plt.plot(x1, model.predict(x1), 'y-', label = 'Best Fit Line')
model.fit(x2, y2)
plt.plot(x1, model.predict(x2), 'y-')
model.fit(x3, y3)
plt.plot(x3, model.predict(x3), 'y-')

#Finishing Plot
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Ratus Juta Jiwa)')
plt.title('Jumlah Penduduk INDONESIA (1971-2010)')
plt.grid(True)
plt.show()

# =========================================
# Summarizing Prediction
# =========================================

print('Prediksi jumlah penduduk Jawa Barat di tahun 2050:', round(int(pred1)))
print('Prediksi jumlah penduduk Bengkulu di tahun 2050:', round(int(pred2)))
print('Prediksi jumlah penduduk INDONESIA di tahun 2050:', round(int(pred3)))
