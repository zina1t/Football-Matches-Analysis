import pandas as pd
import numpy as np
import pingouin
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# load datasets 
men = pd.read_csv('men_results.csv')
women = pd.read_csv('women_results.csv')

# filter data for time range and tournament
men['date'] = pd.to_datetime(men['date'], format="%Y-%m-%d")
men = men[(men['date'] >= '2002-01-01') & (men['tournament'].isin(['FIFA World Cup']))]
men['goals'] = men['home_score'] + men['away_score']

women['date'] = pd.to_datetime(women['date'], format="%Y-%m-%d")
women = women[(women['date'] >= '2002-01-01') & (women['tournament'].isin(['FIFA World Cup']))] 
women['goals'] = women['home_score'] + women['away_score']

# determine if goals distribution is normal
men['goals'].hist()
plt.show()

women['goals'].hist()
plt.show()

# goal distribution is not normal, so perform Wilcoxon-Mann-Whitney test (2 tests with pinguoin and scipy)
results_pg = pingouin.mwu(men['goals'], women['goals'], alternative='greater')
print(results_pg)

results_scipy = mannwhitneyu(men['goals'], women['goals'], alternative='greater')
print(results_scipy)

# extract p-value
p_val = 1 -results_scipy[1]

# determine hypothesis test result with a 10% significance level

a = 0.01
if p_val <= a:
    result = 'reject'
else:
    result = 'fail to reject'
result_dict = {"p_val": p_val, "result": result}

print(result_dict)