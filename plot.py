import pandas as pd
import matplotlib.pyplot as plt 
import re 
df = pd.read_csv('istherecorrelation.csv', sep=';')

columns = df.columns[0]
tokens = re.split(';', columns)

plt.plot(df['Year'],df['NL Beer consumption [x1000 hectoliter]'])
plt.show()