# ************ Compulsory Task 2 ************

''' This program read the movie.xml file, list and displays all the 
child tags of each movie element, displays movie descriptions; and find 
and displays the number of movies that are favourites as well as the 
number of movies that are not favourites.'''

# Import xml.etree.ElementTree library to work with XML files.
import xml.etree.ElementTree as ET

# Loads and parse movie.xml into an ElementTree object.
tree = ET.parse('movie.xml')

# Get the root element of the XML tree.
root = tree.getroot()

# Display the heading for all child tags of each movie element.
print("\n\033[1mList of all child tags of each movie element\033[0m")

# Iterates over movie elements to collect tags of each child element.
for movie in root.iter('movie'):
    # Displays the list of all child tags for each movie element.
    print([child.tag for child in movie])

# Print out the movie descriptions heading.
print("\n\033[1mMovie Descriptions\033[0m")

# Iterate through each description element.
for description in root.iter('description'):
    # Get the description and strip extra whitespaces.
    description_text = "".join(description.itertext()).strip()
    # Display the movie description of each movie element.
    print("\n", description_text)

# Set the initial count of favorite and none favorite movies to zero.
favorite_movies = 0
non_favorite_movies = 0

# Iterates over all movie elements.
for movie in root.iter('movie'):
    # Get the value of the favorite attribute of each movie element.
    favorite = movie.attrib.get('favorite', '').strip().lower()
    # Give condition to count the movies with favourite attribute.
    if favorite == 'true':
        favorite_movies += 1
    # Give condition to count the movies with non-favourite attribute.
    elif favorite == 'false':
        non_favorite_movies += 1

# Display the number of favorite and non-favorite movies.
print(f"\n\033[1mNumber of favorite movies:\033[0m {favorite_movies}")
print(f"\033[1mNumber of non-favorite movies:\033[0m {non_favorite_movies}")
