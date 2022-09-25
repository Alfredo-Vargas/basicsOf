import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")


# Create DataFrame
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Create DataFrame with indices
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Create a DataSeries
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# To read a csv file which has an index column for numbering entries
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

# To write a DataFrime to csv file
fruits.to_csv('./path/to/destination')


