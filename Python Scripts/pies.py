import pandas as pd
from matplotlib import pyplot as plt
# print(plt.style.available)
plt.style.use('tableau-colorblind10')

# Import that Data

raw_data = pd.read_csv('Subject_scores\Math_scores_analysis.csv')
# print(data.head(5))

# Create the DataFrame with the columns that we need to assess to the pie plot
data = pd.DataFrame({
    'Scores': raw_data['Score_Changes'],
    'Goals': raw_data['Goal_Change'],
    'Met or Not': raw_data['Percentage_Kept']
})

# Specify a criteria and create a column that outputs a string that can be counted 

data['Criteria'] = ' '
data.loc[data['Scores'] < data['Goals'], 'Criteria'] += 'Goal Not Achieved'
data.loc[data['Scores'] == data['Goals'], 'Criteria'] += 'Goal Met Exactly'
data.loc[data['Scores'] > data['Goals'], 'Criteria'] += 'Goal Exceeded'
counts = data['Criteria'].value_counts()

# Decorating the plot with a few details
explode = [0.03, .05, 0.03]
colors = ['#ffd7ba', '#83c5be', '#caffbf']

# PLot the pie chart with its necessary arguments
plt.pie(counts.values, labels = counts.index, autopct='%1.2f%%', explode=explode,
        radius=1.08, wedgeprops={'edgecolor' : 'black', 'linewidth': 1} , 
        shadow = True, startangle=40, colors = colors)

# Create a small white circle in the middle to show donut effect
circle1 = plt.Circle((0,0), 0.42, color='black')
circle2 = plt.Circle((0,0), 0.4, color='white', linewidth=1.5, fill=True)
fig = plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)

# Create a text box with a variable that combines two of the percentages together to show how many actually made the goal
#     of keeping thier percentage

count1 = data['Met or Not'].value_counts()
true_met = count1['Yes']
textstr = 'Kept Their Percentage {:.2f}%'.format(true_met / count1.sum() * 100)
props = dict(boxstyle='round', facecolor='lightblue', alpha = 0.5)
plt.text(0.2, .006, textstr, transform=plt.gca().transAxes,
         verticalalignment='center', bbox=props)


# Show the plot and all of its glory

plt.title(' Math MAP Score Goals Met (2016-2017)')
plt.show()


# print(plt.style.available)
plt.style.use('tableau-colorblind10')

raw_data = pd.read_csv('Subject_scores\Reading_scores_analysis.csv')
# print(data.head(5))
data = pd.DataFrame({
    'Scores': raw_data['Score_Changes'],
    'Goals': raw_data['Goal_Change'],
    'Met or Not': raw_data['Percentage_Kept']
})
data['Criteria'] = ' '
data.loc[data['Scores'] < data['Goals'], 'Criteria'] += 'Goal Not Achieved'
data.loc[data['Scores'] == data['Goals'], 'Criteria'] += 'Goal Met Exactly'
data.loc[data['Scores'] > data['Goals'], 'Criteria'] += 'Goal Exceeded'
counts = data['Criteria'].value_counts()
explode = [0.03, .05, 0.03]

colors = ['#ddbea9', '#06d6a0', '#118ab2']
plt.pie(counts.values, labels = counts.index,  autopct='%1.2f%%', explode=explode,
        radius=1.08, wedgeprops={'edgecolor' : 'black', 'linewidth': 1} , shadow = True, startangle=40,
        colors = colors, textprops={'color' : 'black', 'fontsize' : 9})
circle1 = plt.Circle((0,0), 0.42, color='black')
circle2 = plt.Circle((0,0), 0.4, color='white', linewidth=1.5, fill=True)
fig = plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)


count1 = data['Met or Not'].value_counts()
true_met = count1['Yes']
textstr = 'Kept Their Percentage {:.2f}%'.format(true_met / count1.sum() * 100)
props = dict(boxstyle='round', facecolor='lightblue', alpha = 0.5)
plt.text(0.2, 0, textstr, transform=plt.gca().transAxes,
         verticalalignment='center', bbox=props)

plt.title('Reading MAP Goals Met (2016-2017)')
plt.show()

