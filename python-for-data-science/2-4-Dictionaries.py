'''Table of Contents
Dictionaries
What are Dictionaries?
Keys
'''

'''What are Dictionaries?
A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. 
Instead of the numerical indexes such as a list, dictionaries have keys. 
These keys are the keys that are used to access values within a dictionary.
'''

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict) # --> {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5, (0, 1): 6}

# Access to the value by the key
Dict["key1"]

# Access to the value by the key
Dict[(0, 1)]

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

# Get value by keys
print(release_year_dict['Thriller']) # --> 1982

# Get all the keys in dictionary
print(release_year_dict.keys()) # --> dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])

# Get all the values in dictionary
print(release_year_dict.values()) # -->  dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

# Add value with key into dictionary
release_year_dict['Graduation'] = '2007'

# Delete entry by key
del(release_year_dict['Thriller'])

# Verify the key is in the dictionary
print('Thriller' in release_year_dict) # --> False
print('The Bodyguard' in release_year_dict) # --> True
