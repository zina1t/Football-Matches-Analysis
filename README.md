# Football-Matches-Analysis
Exploratory Data Analysis of men and women matches.

## Football
This is a Jupyter Notebook which will contain plots and analysis of football matches. 

## Dataframe:

The **results** dataframe has following columns:

1. **date**: date of the match
2. **home_team**: the name of the home team.
3. **away_team**: the name of the away team.
4. **home_score**: full-time home team score.
5. **away_score**: full-time away team score.
6. **tournament**: the name of the tournament.

## Key Findings

1. Proportion of the friendly matches has decreased.
2. The number of goals per match has gone downward.
3. Brazil, Germany and Spain have the best winning ratios.
4. Germany, Brazil, England are some of the best attacking teams.
5. Iran, Morocco and Brazil are some of the best defending teams.

## Goals_diff
goals_diff.py is a file of DataCamp Project
### Instructions
Perform an appropriate hypothesis test to determine the p-value, and hence result, of whether to reject or fail to reject the null hypothesis that the mean number of goals scored in women's international soccer matches is the same as men's. Use a **10% significance level**.

For this analysis, you'll use Official **FIFA World Cup** matches since **2002-01-01**, and you'll also assume that each match is fully independent, i.e., team form is ignored.

The p-value and the result of the test must be stored in a dictionary called **result_dict** in the form:

**result_dict = {"p_val": p_val, "result": result}**

where **p_val** is the p-value and result is either the string **"fail to reject"** or **"reject"**, depending on the result of the test.
