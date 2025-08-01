import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\TAHIR\Downloads\social_media_engagement_file.csv')

# Group and pivot the data
pivot_df = df.groupby(['post_type', 'platform'])['engagement_score'].mean().unstack()

# Plot
pivot_df.plot(kind='bar', figsize=(10, 6), colormap='Set2')

# Chart formatting
plt.title('Best Performing Content Type by Platform (Engagement Score)')
plt.ylabel('Average Engagement Score')
plt.xlabel('Post Type')
plt.xticks(rotation=45)
plt.legend(title='Platform')
plt.tight_layout()
plt.show()
