import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# print(plt.style.available)
plt.style.use('_classic_test_patch')
math = pd.read_csv('subject_scores\Math_scores_analysis.csv')
# print(math.head(4))
reading = pd.read_csv('subject_scores\Reading_scores_analysis.csv')
raw_data = pd.read_csv('KIPP_unedited\map_scores.csv')
print(raw_data.head())

# datam = raw_data[raw_data['typical_fall_to_spring_growth'].notnull()]
# datag = datam[datam['typical_fall_to_spring_growth'].notna()]
# mean_change = np.mean(datag['typical_fall_to_spring_growth'])
# print(mean_change)

math_scores = pd.DataFrame({
    'Fall 2017':math['Fall_Math_rit_score'],
    'Spring 2017': math['Spring_Math_rit_score'],
})

reading_scores = pd.DataFrame({
    'Fall 2017':reading['Fall_Reading_rit_score'],
    'Spring 2017': reading['Spring_Reading_rit_score'] 
})


bp = math_scores.boxplot(column = ['Fall 2017', 'Spring 2017'], grid = False)
gox = reading_scores.boxplot(column = ['Fall 2017', 'Spring 2017'], grid = False, )
bp.plot()
gox.plot()
plt.ylim(90,270)
plt.title('Math Rit Score Comparison')
plt.show()







