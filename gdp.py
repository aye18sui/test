import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Users\65747\Downloads\GDP.xlsx')
# print(df.head(5))
# print(df[2:4])
# print(df[['province','2019_gdp']].head(5))
# print(df.iloc[0:3,0:3])
df=df[['province','2010_gdp','2019_gdp']]
df=df.set_index('province')
df.columns='2010','2019'
df['2010'] = df['2010']/1e4
df['2019'] = df['2019']/1e4
df['increase'] = (df['2019'] - df['2010']) / df['2010']
print(df.head())
import matplotlib.pyplot as plt
#df['2019'].plot(kind='bar')
plt.rcParams['font.sans-serif']=['SimHei']#加载字体
plt.rcParams['axes.unicode_minus']=False #保存图形是-
# plt.show()
df = df.sort_values(by='increase', ascending=False)
print(df.head(5))
df['increase'].plot(kind='bar')
plt.title('2019年各省GDP较2010增幅')
plt.ylabel('gdp_increase')
plt.show()