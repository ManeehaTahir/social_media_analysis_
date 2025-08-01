import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')

top_categories = df['post_type'].value_counts().head(5)
colors = plt.get_cmap('Set2').colors
#df.plot(kind='barh', x='post_type', y='engagement_score', figsize=(10, 6))

top_categories.plot.barh(color=colors[:5])
plt.xlabel('engagement_score')
plt.ylabel('post_type')
plt.title('viral_posts')
plt.Colormap('Set2')
plt.show()
