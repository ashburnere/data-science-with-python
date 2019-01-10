'''
Table of Contents
About the Dataset
Tuples
Indexing
Slicing
Sorting
'''

'''About the Dataset
Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.
The table has one row for each album and several columns:

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

# Create your first tuple
tuple1 = ("disco",10,1.2 )
print(tuple1) # --> ('disco', 10, 1.2)

# print index of element 'disco'
print(tuple1.index("disco")) # --> 0

# Print the type of the tuple you created
print(type(tuple1)) # --> <class 'tuple'>
# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
print(tuple1[-1]) # --> 1.2
# Use negative index to get the value of the second last element
print(tuple1[-2]) # --> 10

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2) # --> ('disco', 10, 1.2, 'hard rock', 10)

# Slice from index 0 to index 2
print(tuple2[0:3]) # --> ('disco', 10, 1.2)

# Slice from index 3 to index 4
print(tuple2[3:5]) # --> ('hard rock', 10)

# Get the len
print(len(tuple2))

# A sample tuple
ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
# Sort the tuple
ratingsSorted = sorted(ratings)
print(ratings) # --> (0, 9, 6, 5, 10, 8, 9, 6, 2)
print(ratingsSorted) # --> [0, 2, 5, 6, 6, 8, 9, 9, 10]
print(type(ratingsSorted)) # --> <class 'list'>

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print the first element in the second nested tuples
print(NestedT[2][1][0]) # --> r

