import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')


sns.boxplot(x='Cleaned_Sentiment', y='engagement_score', data=df, palette="pastel")
plt.title('Engagement by Sentiment')
plt.show()