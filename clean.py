import pandas as pd
data = pd.read_csv("artwork_data.csv", low_memory=False)

#****************************************************************

# Step 1: Understanding Data
# Conduct the steps from the video, edit and run the code

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


#****************************************************************

# Step 3: Index and Filter 


#****************************************************************

# Step 4: Handle Bad Data
# Remove whitespace, replace bad data, drop rows of data, 
# and remove duplicate data for the artist artwork dataset



