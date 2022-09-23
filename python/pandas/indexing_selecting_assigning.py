import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Select a single column
desc = reviews["description"]

# Get the first value of the decription column (3 ways)
desc[0]
reviews.description[0]
reviews.description.loc[0]
reviews.description.iloc[0]  # preferable method

# Select the first row of a dataframe
first_row = reviews.iloc[0]

# Select first 10 elements of description
first_descriptions = reviews.description.iloc[0:10]
first_descriptions = reviews.description.iloc[:10]

# Select specific rows
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]

# iloc vs loc
# iloc selects similarly to Python (excludes last term) while loc includes last term

# To select some rows and some columns
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

# Select 100 first entries of two specific columns
df = reviews.loc[0:99, ['country', 'variety']]

# to select a series given a logical condition
italian_wines = reviews.country == 'Italy'

# to select a dataframe given a logical condition
italian_wines = reviews.loc[reviews.country == 'Italy']

# Select top_oceania_wines with at least 95 points for wines
# from Australia or New Zealand
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points >= 95)]
