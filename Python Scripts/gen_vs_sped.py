import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('classic')

# import data
raw_data = pd.read_csv('Sp_Ed_scores\Gen_ed_Math.csv')
raw_data2 = pd.read_csv('Sp_Ed_scores\Gen_ed_Reading.csv')
raw_data3 = pd.read_csv('Sp_Ed_scores\SPED_only_Math.csv')
raw_data4 = pd.read_csv('Sp_Ed_scores\SPED_only_Reading.csv')
raw_data5 = pd.read_csv('Sp_Ed_scores\Gifted_Math.csv')
raw_data6 = pd.read_csv('Sp_Ed_scores\Gifted_Reading.csv')


# Math Scores Among Gen Ed
data = pd.DataFrame({
    'Students_id': raw_data['student_id'],
    'Fall': raw_data['Fall_Math_rit_score'],
    'Spring': raw_data['Spring__Math_rit_score'],
    'Changes': raw_data['Score_Changes']
})

# Reading Scores Among Gen Ed
data2 = pd.DataFrame({
    'Students_id': raw_data2['student_id'],
    'Fall': raw_data2['Fall_Reading_rit_score'],
    'Spring': raw_data2['Spring_Reading_rit_score'],
    'Changes': raw_data2['Score_Changes']
})

# Math Scores Among Spec Ed
data3 = pd.DataFrame({
    'Students_id': raw_data3['student_id'],
    'Fall': raw_data3['Fall_Math_rit_score'],
    'Spring': raw_data3['Spring_Math_rit_score'],
    'Changes': raw_data3['Score_Changes']
})

# Reading Scores Among Spec Ed
data4 = pd.DataFrame({
    'Students_id': raw_data4['student_id'],
    'Fall': raw_data4['Fall_Reading_rit_score'],
    'Spring': raw_data4['Spring_Reading_rit_score'],
    'Changes': raw_data4['Score_Changes']
})

# Math Scores Among Spec Ed
data5 = pd.DataFrame({
    'Students_id': raw_data5['student_id'],
    'Fall': raw_data5['Fall_Math_rit_score'],
    'Spring': raw_data5['Spring_Math_rit_score'],
    'Changes': raw_data5['Score_Changes']
})

# Reading Scores Among Spec Ed
data6 = pd.DataFrame({
    'Students_id': raw_data6['student_id'],
    'Fall': raw_data6['Fall_Reading_rit_score'],
    'Spring': raw_data6['Spring_Reading_rit_score'],
    'Changes': raw_data6['Score_Changes']
})


# Calculate the mean for each plot in both Special education and General Education
# I first wanted to do the mode, yet it does nothing really

mode_gm = round(data['Changes'].mean(),2)
mode_gr = round(data2['Changes'].mean(),2)
mode_sm = round(data3['Changes'].mean(),2)
mode_sr = round(data4['Changes'].mean(),2)
mode_gfm = round(data5['Changes'].mean(),2)
mode_gfr = round(data6['Changes'].mean(),2)


# Plot the points in general
plt.hist(data['Changes'], bins = 30, alpha = 0.6, color = '#005f73', label = 'General Education', edgecolor='black')

# plot the mode of each histogram to show the most improvement between each program
plt.annotate(f'AVG Improvement(Gen Ed): {mode_gm}', xy=(mode_gm,80),
             xytext=(mode_gm + 10, 100), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize = 10)

# Plot the points in general
plt.hist(data3['Changes'],bins = 30, alpha = 1, color = '#e9d8a6', label = 'Special Education', edgecolor = 'black')

# plot the mode of this histogram
plt.annotate(f'AVG Improvement(Sp Ed): {mode_sm}', xy=(mode_sm,6),
             xytext=(35, 50), arrowprops=dict(facecolor='black', arrowstyle='<-'), fontsize=10)

# Plot the points in general
plt.hist(data5['Changes'],bins = 30, alpha = 1, color = '#ae2012', label = 'Gifted', edgecolor = 'black')

# plot the mode of this histogram
plt.annotate(f'AVG Improvement(Gifted): {mode_gfm}', xy=(mode_gfm,2),
             xytext=(-35, 90), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Decorators to show what is plotted

plt.title('Gen Edu. vs Spec Edu. Programs \n Math Improvement')
plt.legend(loc='upper right', borderaxespad=0.1, frameon=True)
plt.xlabel('Growth in Scores')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Next chart

plt.style.use('classic')

# Plot the points in general
plt.hist(data2['Changes'], bins = 30, alpha = 0.6, color = '#005f73', label = 'General Education', edgecolor='black')

# plot the mode of this histogram
plt.annotate(f'AVG Improvement(Gen Ed): {mode_gr}', xy=(mode_gr,100),
             xytext=(mode_gr + 22, 80), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Plot the points in general
plt.hist(data4['Changes'], bins = 30, alpha = 1, color = '#e9d8a6', label = 'Special Education', edgecolor='black')

# plot the mode of this histogram
plt.annotate(f'AVG Improvement(Sp Ed): {mode_sr}', xy=(mode_sr,7),
             xytext=(34, 35), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize = 10)

# Plot the points in general
plt.hist(data6['Changes'],bins = 30, alpha = 1, color = '#ae2012', label = 'Gifted', edgecolor = 'black')

# plot the mode of this histogram

plt.annotate(f'AVG Improvement(Gifted): {mode_gfr}', xy=(mode_gfr,2),
             xytext=(-39, 90), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Decorators to show what i am plotting

plt.title('Gen Edu. vs Sp Ed Programs \n Reading Improvement')
plt.legend(loc='upper right', borderaxespad=0.1, frameon=True)
plt.ylim(0,130)
plt.xlabel('Growth in Scores')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

