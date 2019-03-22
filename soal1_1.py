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
# print(df.tail(10))

# =========================================
# Plotting
# =========================================

plt.style.use('ggplot')

#Plot Provinsi Penduduk Terbanyak 2010
dfx = df.drop(df.tail(1).index)
# print(dfx)
dfprovmax2010 = dfx.loc[dfx.index[dfx[2010]==dfx[2010].max()]]
# print(dfprovmax2010)
x = dfprovmax2010.columns.values
# print(x)
y = dfprovmax2010.values.reshape(6,)
# print(y)
plt.plot(x, y, 'g-', label = ''.join(dfprovmax2010.index.values))
plt.scatter(x, y, color = 'g')

#Plot Provinsi Penduduk Tesedikit 1971
dfprovmin1971 = df.loc[df.index[df[1971]==df[1971].min()]]
# print(dfprovmin1971)
x = dfprovmin1971.columns.values
# print(x)
y = dfprovmin1971.values.reshape(6,)
# print(y)
plt.plot(x, y, 'b-', label = ''.join(dfprovmin1971.index.values))
plt.scatter(x, y, color = 'b')

#Plot Jumlah Penduduk Indonesia
dfsumcitizen = df.tail(1)
# print(dfsumcitizen)
x = dfsumcitizen.columns.values
# print(x)
y = dfsumcitizen.values.reshape(6,)
# print(y)
plt.plot(x, y, 'r-', label = ''.join(dfsumcitizen.index.values))
plt.scatter(x, y, color = 'r')

#Finishing Plot
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Ratus Juta Jiwa)')
plt.title('Jumlah Penduduk INDONESIA (1971-2010)')
plt.grid(True)
plt.show()
