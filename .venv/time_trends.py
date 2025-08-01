import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')


day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Set 'post_day' column to ordered categorical
df['post_day'] = df['post_day'].astype(CategoricalDtype(categories=day_order, ordered=True))

# Plot
sns.lineplot(x='post_day', y='engagement_score', data=df, marker='o')
plt.title('Engagement by Day of Week')
plt.xlabel('Day')
plt.ylabel('Engagement Score')
plt.grid(True)
plt.tight_layout()
plt.show()