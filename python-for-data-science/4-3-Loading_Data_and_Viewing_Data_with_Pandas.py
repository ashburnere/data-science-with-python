'''Table of Contents
About the Dataset
Viewing Data and Accessing Data with pandas
'''

'''About the Dataset
The table has one row for each album and several columns

artist - Name of the artist
album - Name of the album
released_year - Year the album was released
length_min_sec - Length of the album (hours,minutes,seconds)
genre - Genre of the album
music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
date_released - Date on which the album was released
soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
rating_of_friends - Indicates the rating from your friends from 1 to 10
'''

import pandas as pd

# read from file
csv_path='D:/WORKSPACES/data-science-with-python/resources/data/top_selling_albums.csv'
# read from url
#csv_path='https://ibm.box.com/shared/static/keo2qz0bvh4iu6gf5qjq4vdrkt67bvvb.csv'
df = pd.read_csv(csv_path)

# We can use the method head() to examine the first five rows of a dataframe:
print("top 5 rows\n", df.head())

#We use the path of the excel file and the function read_excel. The result is a data frame as before:
# xlsx_path='https://ibm.box.com/shared/static/mzd4exo31la6m7neva2w45dstxfg5s86.xlsx'
# df = pd.read_excel(xlsx_path)
#df.head()

# We can access the column "Length" and assign it a new dataframe 'x':
x=df[['Length']]
print(x)

'''
Viewing Data and Accessing Data 
'''

# You can also assign the value to a series, you can think of a Pandas series as a 1-D dataframe. Just use one bracket:
x=df['Length']
print(type(x))

# You can also assign different columns, for example, we can assign the column 'Artist':
x=df[['Artist']]
print(type(x))

y=df[['Artist','Length','Genre']]
print(type(y))

# print value of first row first column
print(df.iloc[0,0]) # --> Michael Jackson
print(df.loc[0,'Artist']) # --> Michael Jackson

# slicing
print(df.iloc[0:2, 0:3])
print(df.loc[0:2, 'Artist':'Released'])