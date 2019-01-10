'''Table of Contents
Sets
Set Content
Set Operations
Sets Logic Operations
'''

'''Set
A set is a unique collection of objects in Python. 
You can denote a set with a curly bracket {}. Python will automatically remove duplicate items:
'''

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1) # --> {'pop', 'soul', 'rock', 'hard rock', 'disco', 'R&B'}

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)  
print( album_set ) # --> {65, 'Michael Jackson', 'Thriller', 10.0, 46.0, '00:42:19', 'Pop, Rock, R&B', '30-Nov-82', None, 1982}

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"])
'''
Set Operations
'''
# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
# Add element to set
A.add("NSYNC")
# Try to add duplicate element to the set --> no change
A.add("NSYNC")
# Remove the element from set
A.remove("NSYNC")

# Verify if the element is in the set
isIn = "AC/DC" in A
print(isIn) # --> True

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections
intersection = album_set1 & album_set2
print(intersection) # --> {"AC/DC", "Back in Black"}
# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2))   # --> {"AC/DC", "Back in Black"}


# Find the difference in set1 but not set2
diff = album_set1.difference(album_set2) 
print(diff) # --> {'Thriller'}

# The elements in album_set2 but not in album_set1 is given by:
diff = album_set2.difference(album_set1) 
print(diff) # --> {'The Dark Side of the Moon'}

# Find the union of two sets
union = album_set1.union(album_set2)
print(union) # --> {'The Dark Side of the Moon', 'AC/DC', 'Thriller', 'Back in Black'}

# Check if superset
print(album_set1.issuperset(album_set2))
# Check if subset
print(album_set1.issubset(album_set2))

# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1)) # --> True
# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))  # --> True