from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('classic')
# Random test data
math = pd.read_csv('Subject_scores\Math_scores_analysis.csv')
reading = pd.read_csv('Subject_scores\Reading_scores_analysis.csv')
math_scores = pd.DataFrame({
    'Fall 2017':math['Fall_Math_rit_score'],
    'Spring 2017': math['Spring_Math_rit_score'],
})
reading_scores = pd.DataFrame({
    'Fall 2017': reading['Fall_Reading_rit_score'],
    'Spring 2017': reading['Spring_Reading_rit_score'] 
})

median_fm = np.median(math_scores['Fall 2017'])
median_sm = np.median(math_scores['Spring 2017'])
median_fr = np.median(reading_scores['Fall 2017'])
median_sr = np.median(reading_scores['Spring 2017'])

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
labels = ['Fall 2016', 'Spring 2017']
# notch box plot 1
bplot1 = ax1.boxplot(math_scores,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax1.set_title('Comparing Math RIT Scores')

ax1.plot([1,2], [median_fm, median_sm], color = 'black', linewidth = 1.8, linestyle='--', dashes = (3,3))


ax1.text(1.5, (median_fm + median_sm)/3, 'Median Difference: {:.2f}'.format(abs(median_fm-median_sm)),
         ha='center', va='center', fontsize = 9)

plt.style.use('classic')

# notch shape box plot 2
bplot2 = ax2.boxplot(reading_scores,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax2.set_title('Comparing Reading RIT Scores')

# fill with colors
colors = ['#2a9d8f', '#03045e']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

# adding horizontal grid lines
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Semesters')
    ax.set_ylabel('RIT Scores')


# Add a line connecting the notches between boxes
ax2.plot([1,2], [median_fr, median_sr], color = 'black', linewidth = 1.8, linestyle='--', dashes=(3,3))

ax2.text(1.5, (median_fr + median_sr)/3, 'Median Difference: {:.2f}'.format(abs(median_fr-median_sr)),
         ha='center', va='center', fontsize = 9)

plt.show()

