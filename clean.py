from email import header
import pandas as pd
data = pd.read_csv("artwork_sample.csv")

#****************************************************************

# Step 1: Understanding Data
# Conduct the steps from the video, edit and run the code

# Viewing and Converting Types
# print(data.head())
# print(data.dtypes)
# print(data.acquisitionYear)
# print(data.acquisitionYear.astype(float))
# print(data.acquisitionYear.dtype)
# data.acquisitionYear = data.acquisitionYear.astype(float)
# print(data.acquisitionYear.dtype)
# fulldf = pd.read_csv("artwork_data.csv", low_memory=False)
# print(fulldf.head())
# print(fulldf.dtypes)
# print(fulldf.height.astype(float))
# print(pd.to_numeric(fulldf.height, errors="coerce"))
# print(pd.to_numeric(fulldf.height, errors="coerce"[41339]))
# print(fulldf.height.dtype)
# fulldf.height = pd.to_numeric(fulldf.height, errors="coerce")
# print(fulldf.height.dtype)

# Aggregate Data
# print(data.head())
#print(data.year)
# print(data.year.min())
# print(data.year.max())
# print(data.year.sum())
# print(data.year.mean())
# print(data.year.std())
# print(data.artist.min())
#print(data.artist.mean())
# print(data.artist.sum())
# print(data.sum())
# print(data.agg('min'))
# print(data.agg(['min', 'max']))
# print(data.agg(['min', 'max','mean', 'std']))
# print(data.agg('mean', axis="columns"))

# Normalize Data
# print(data.head())
# print(data.dtypes)
# print(data.height.mean())
# print(data.artist.mean())
# print(data.height)
# print(data.height.min())
# print(data.height.max())
# print(data.height.mean())
# print(data.height.std())
# height = data.height
# norm = (height - height.mean()) / height.std()
#  print(norm)
# minmax = (height - height.min()) / (height.max() - height.min())
# print(minmax)
# print(minmax.min())
# print(minmax.max())
# print(data)
# data.height = minmax
# data['standardized_height'] = norm
# data.new_column = norm
# print(data.head())

#Transforming Data
# print(data.height.transform(lambda x: print(x)))
# print(data.height.transform(lambda x: x))
# print(data.height.transform(lambda x: x / 10))
# print(data.groupby('artist'))
# print(data.groupby('artist').transform('nunique'))
# print(data.groupby('artist')['height'])
# print(data.groupby('artist')['height'].transform('mean'))
# print(data.artist)
# data['mean_height_by_artist'] = data.groupby('artist')['height'].transform('mean')
# print(data)

# Filtering Data
# print(data.head())
# print(data.filter(items=['id', 'artist']))
# print(data.filter(like='year'))
# print(data.filter(like='artist'))
# print(data.filter(regex="(?i)year"))
# print(data.filter(axis=0, regex="^100.$"))
# print(data.filter(regex="^100(0|2|4|6|8)$", axis=0))

#****************************************************************

# Step 2: Remove and Fix columns
# Drop, change, and rename columns

# Dropping Columns
# print(data.head())
# print(data.drop(0))
# print(data.drop('id'))
# print(data.drop('id', axis=1))
# print(data.drop(columns=['id']))
# print(data.drop(columns=['height', 'width', 'depth']))
# print(data.head())
# print(data.drop(labels=[0,1,2]))
# print(data)
# data.drop(columns=['id'], inplace=True)
# print(data)
# data.drop(columns=['id'])
# data = pd.read_csv("artwork_sample.csv", usecols=['artist','title'])
# print(data.head())

# Changing column casing
# print(data.columns)
# print(data.columns.str.lower())
# [x.lower() for x in data.columns]
# data.columns = [x.lower() for x in data.columns]
# print(data.columns)
# data.columns = map(lambda x: x.lower(), data.columns)
# print(data.columns)
# print(data.columns)
# import re
# data.columns = [re.sub(r'([A-Z])', r'_\1', x).lower() for x in data.columns]
# print(data.columns)

# Renaming Columns 
# print(data.columns)
# print(data.rename(columns={"thumbnailUrl": "thumbnail"}))
# print(data.rename({"thumbnailUrl" : "thumbnail"}, axis=1))
# print(data)
# print(data.rename(columns={"thumbnailUrl" : "thumbnail"}, inplace=True))
# print(data)
# print(data.rename(columns=lambda x: x.lower(), inplace=True))
# print(data.columns)
# data.columns = ['id', 'AccessionNumber', 'Artist', 'ArtistRole', 'artistid', 'title',
#        'datetext', 'medium', 'creditline', 'year', 'acquisitionyear',
#        'dimensions', 'width', 'height', 'depth', 'units', 'inscription',
#        'thumbnailcopyright', 'thumbnailurl', 'url']
# print(data.columns)
# data = pd.read_csv("artwork_sample.csv", names=['id', 'AccessionNumber', 'Artist', 'ArtistRole', 'artistid', 'title',
#        'datetext', 'medium', 'creditline', 'year', 'acquisitionyear',
#        'dimensions', 'width', 'height', 'depth', 'units', 'inscription',
#        'thumbnailcopyright', 'thumbnailurl', 'url'], header=0)
# print(data.columns)

#****************************************************************

# Step 3: Index and Filter 

# Direct Filterting with Square Brackets
# print(data.head())
# print(data['id'])
# print(data['id'][1])
# print(data[['artist', 'title']])
# print(data[['artist', 'title']][1]) throws error
# print(data[['artist', 'title']]['artist'])
# print(data[['artist', 'title']]['artist'][1])
# print(data[1]) throws error
# print(data[1:2])
# print(data[1:5])
# print(data[1:5]['artist'])
# print(data[data['year'] > 1800])
# print(data[data['year'] > 1800]['year'])

# Data Indexing with .loc
# print(data.head())
# print(data.loc[ROWS, COLS]) standard format for loc
# print(data.loc[0, :])
# print(data.loc[0:2, :]) includes rows 0-2, loc in inclusive
# print(data[0:2]) is exclusive, inlcudes rows 0-1
# print(data.loc[0:2, 'title'])
# print(data.loc[0:2, ['artist', 'title']])
# print(data.loc[[1,5], ['artist', 'title']])
# print(data.head())
# print(data.loc[[1,5], 'id': 'artistId'])
# print(data.loc[data.artist == 'Blake, Robert', :])
# print(data.loc[data.artist == 'Blake, Robert', ['title', 'year']])

# Using .iloc to Access Specific Rows or Columns
# print(data.head())
# print(data.iloc[0, :])
# print(data.iloc[0:3, :])  iloc is exclusive
# print(data.loc[0:3, :])
# print(data.head())
# print(data.iloc[0:3, :])
# print(data.loc[0:3, :]) throws error
# print(data.loc[1035:1037, :])
# print(data.iloc[0:3, 0:3])
# data.reset_index(inplace=True)
# print(data.head())
# print(data.iloc[0:3, 0:3])
# print(data.iloc[[5,8],[0,2]])

# Filtering Data with str.contains
# print(data.head())
# print(data.medium)
# print(type(data.medium))
# print(data.medium.str)
# print(data.medium.str.contains('Graphite'))
# print(data.loc[data.medium.str.contains('Graphite'), ['artist', 'medium']])
# print(data.head())
# print(data.loc[data.medium.str.contains('Graphite', case=False), ['artist', 'medium']])
# print(data.loc[data.medium.str.contains('(?i)Graphite', regex=True), ['artist', 'medium']])
# print(data.loc[data.medium.str.contains('(?i)Graphite', regex=True) | data.medium.str.contains('(?i)Line', regex=True), ['artist', 'medium']])
# print(data.loc[data.medium.str.contains('graphite|line', case=False, regex=True), ['artist', 'medium']])
# print(data.dtypes)
# print(data.year.str.contains('1826')) throws error, applying str methods to a float
# print(data.year.astype(str).str.contains('1826'))
# print(data.loc[data.year.astype(str).str.contains('1826')])
# data = pd.read_csv("artwork_data.csv", low_memory=False)
# print(data.head())
# print(data.loc[data.dimensions.str.contains('support')]) throws an error, some of the values include NaN
# print(data.loc[data.dimensions.str.contains('support', na=False)])

#****************************************************************

# Step 4: Handle Bad Data
# Remove whitespace, replace bad data, drop rows of data, 
# and remove duplicate data for the artist artwork dataset



