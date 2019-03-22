import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    'indo_12_1.xls', 
    header = 3, 
    names = ['provinsi', 1971, 1980, 1990, 1995, 2000, 2010],
    na_values = ['-', 'NaN']
)
df = df.set_index('provinsi')
df = df.interpolate()
print(df.head(10))

Bengkulu = np.array(df.iloc[6])
Jabar = np.array(df.iloc[11])
Indonesia = np.array(df.iloc[33])

# print(Bengkulu)
# print(Jabar)
# print(Indonesia)

plt.style.use('ggplot')
plt.plot(Bengkulu, 'b-', marker = 'o', label = 'Bengkulu')
plt.plot(Jabar, 'g-', marker = 'o', label = 'Jawa Barat')
plt.plot(Indonesia, 'r-', marker = 'o', label = 'INDONESIA')
# plt.plot(Bengkulu, 'b-', label = 'Bengkulu')
# plt.plot(Jabar, 'g-', label = 'Jawa Barat')
# plt.plot(Indonesia, 'r-', label = 'INDONESIA')
plt.legend()
# plt.scatter(df[[1971, 1980, 1990, 1995, 2000, 2010]], Bengkulu, 'b-', color = 'b')
# plt.scatter(df[[1971, 1980, 1990, 1995, 2000, 2010]], Jabar, 'g-', color = 'g')
# plt.scatter(df[[1971, 1980, 1990, 1995, 2000, 2010]], Indonesia, 'r-', color = 'r')
plt.xticks(np.arange(6), (1971, 1980, 1990, 1995, 2000, 2010))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Ratus Juta Jiwa)')
plt.title('Jumlah Penduduk INDONESIA (1971-2010)')
plt.grid(True)

plt.show()
