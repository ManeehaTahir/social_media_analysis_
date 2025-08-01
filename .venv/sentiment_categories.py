import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')

data_for_pie = df['Cleaned_Sentiment'].value_counts()
colors = ['gold', 'yellowgreen', 'lightcoral']
plt.pie(data_for_pie, labels=data_for_pie.index, autopct='%.1f%%', startangle=90, colors=colors)
plt.title('Sentiment Categories')
plt.show()