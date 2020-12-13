import pandas as pd

Spent = pd.read_csv(
    '/Users/matthew.bonick/Avira/Sascha Halder - sascha-matthew/Forecasting Notebooks/2021 Forecast/Marketing Spent.csv')

print(Spent)

## edit and clean spent data
Spent.rename(columns={"_col1": 'spent'}, inplace=True)
