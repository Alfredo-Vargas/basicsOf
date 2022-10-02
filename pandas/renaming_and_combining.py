import pandas as pd

pd.set_option('max_rows', 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# change column(s) name(s)
reviews.rename(columns={'points': 'score'})

# region_1 and region_2 are pretty uninformative names for locale columns in the dataset. 
# Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

# change row name
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# Set the index name in the dataset to wines
reindexed = reviews.rename_axis('wines', axis='rows')

# set_index is sometimes more convenient when renaming
# changing the row and column indices names
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# combining in pandas: concat(), join(), and merge()
# whenever we have the same fields (columns)
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
pd.concat([canadian_youtube, british_youtube])

# The [Things on Reddit](https://www.kaggle.com/residentmario/things-on-reddit/data) dataset includes product links
# from a selection of top-ranked forums ("subreddits") on reddit.com. 
# Run the cell below to load a dataframe of products mentioned on the */r/gaming* subreddit and another dataframe for products mentioned on the *r//movies* subreddit.
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
# Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])

# whenever the dataframe to combine have an index in common, then:
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')
# The lsuffix and rsuffix parameters are necessary here because
# the data has the same column names in both British and Canadian datasets. 
# If this wasn't true (because, say, we'd renamed them beforehand) we wouldn't need them.

# The [Powerlifting Database](https://www.kaggle.com/open-powerlifting/powerlifting-database) dataset on Kaggle
# includes one CSV table for powerlifting meets and a separate one for powerlifting competitors. 
# Run the cell below to load these datasets into dataframes:
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
# Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. 
# Using this, generate a dataset combining the two tables into one.
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index('MeetID'))
