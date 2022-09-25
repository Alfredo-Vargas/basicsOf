import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Get the median of a given column
median_points = reviews.points.median()

# Get distinct elements of a column
countries = reviews.country.unique()

# How often does each country appear in the dataset, cummulative sum per type
reviews_per_country = reviews.country.value_counts()

# Create a variable centered_price containing a version of the price column with the mean price subtracted
mean_price = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - mean_price)

# Which wine is the "best bargain"?
points_price_ratio = reviews.points / reviews.price
bargain_index = points_price_ratio.idxmax()
bargain_wine = reviews.loc[bargain_index, 'title']

# Which word is used more when describing a wine? "tropical" or "fruity"?
n_tropical = reviews.description.map(lambda t: "tropical" in t).sum()
n_fruity = reviews.description.map(lambda t: "fruity" in t).sum()
descriptor_counts = pd.Series([n_tropical, n_fruity], index=['tropical', 'fruity'])

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
# Create a series star_ratings with the number of stars corresponding to each review in the dataset.
def get_stars(entry):
    if entry.country == 'Canada':
        return 3
    elif entry.points >= 95:
        return 3
    elif entry.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(get_stars, axis='columns')
