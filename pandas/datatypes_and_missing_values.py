import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)

# check datatype of entire dataframe
reviews.dtypes

# check datatype of a particular column
reviews.price.dtype

# convert type of a particular column it returns a pandas series
reviews.points.astype('float64')

# dataframe or series index has its own datatype
reviews.index.dtype

# for technical reasons NaN values are of the 'float64' dtype
# we can filter missing on non missing values as follows
reviews[pd.isnull(reviews.country)]
reviews[pd.notnull(reviews.country)]

# check how many values are missing from a particular attribute
n_missing_prices = reviews[pdf.isnull(reviews.price)]
n_missing_prices = reviews.price.isnull().sum()
n_missing_prices = pd.isnull(reviews.price).sum()

# replacing missing values
reviews.region_2.fillna("Unknown")

# replace a non-null value
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# what are the most common wine-producing regions? 
# Create a Series counting the number of times each value occurs in the region_1 field. 
# This field is often missing data, so replace missing values with Unknown. 
# Sort in descending order. Your output should look something like this:
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
