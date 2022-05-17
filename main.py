'''GUF'''
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('udemy_courses.csv')
fig, ax = plt.subplots(2)
levels = data['level'].unique()
avgs = []
cols1 = []
for i in levels:
    level = data.loc[data['level'] == i]
    avgs.append(level['content_duration'].sum()/len(level['content_duration']))
    cols1.append(i)
subjects = data['subject'].unique()
nums = []
cols2 = []

for i in subjects:
    subject = data.loc[data['subject'] == i]
    nums.append(len(subject['course_id']))
    cols2.append(i)
ax[0].bar(cols1, avgs)
ax[1].bar(cols2, nums)
fig.set_figwidth(10)
plt.show()
