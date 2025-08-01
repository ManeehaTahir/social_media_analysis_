import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')
print(df.head())

data=df
plt.bar(data.platform,data.engagement_score,tick_label=data.platform, color='purple')
plt.title('Platform Analysis')
plt.xlabel('Platform')
plt.ylabel('Engagement Score')
plt.show()