# Read in the movies.txt file. Each separate line is a description of a different movie.
# Your task is to create a function to return which movies a user would watch
# next if they have watched Planet Hulk with the description “Will he save
# their world or destroy it? When the Hulk becomes too dangerous for the
# Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
# planet where the Hulk can live in peace. Unfortunately, Hulk land on the
# planet Sakaar where he is sold into slavery and trained as a gladiator.”

# The function should take in the description as a parameter and return the
# title of the most similar movie.

import spacy  
nlp = spacy.load('en_core_web_md')

def recommended_movies():

# read movies.txt and create a list of sentences
    try:
        with open(r'movies.txt', 'r', encoding = "utf-8") as file:
            movie_list = []
            for line in file:
                movie_list.append(line)
    except FileNotFoundError:
        print("Error: File not found.")
    except:
        print("An error occurred while reading the file.")

    # create a variable to hold the description of Planet Hulk
    planet_hulk = nlp("""
    Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.
    """)

    # create an empty list to hold the most similar movie
    most_similar = []

    # loop through the other movie descriptions to compare them to Planet Hulk
    for sentence in movie_list:

    # split the senence to isolate the plot description
        split_sentence = sentence.split(" :")

    # compare the 2 plots
        similarity = nlp(split_sentence[1]).similarity(planet_hulk)

    # if the most_similar list is empty add this movie
        if not most_similar:
            most_similar.extend([split_sentence[0], split_sentence[1], similarity]) 

    # else assess if the movie on the list is more or less similar than this one, and replace it if the movie on the current loop 
    # is more similar
        else:
            if most_similar[2] > similarity:
                continue
            elif most_similar[2] == similarity:
                most_similar.extend([split_sentence[0], split_sentence[1], similarity]) 
            elif most_similar[2] < similarity:
                del most_similar[:]
                most_similar.extend([split_sentence[0], split_sentence[1], similarity]) 

    # there's a chance that the list could include more than one movie with the same similarity score, handling eventuality below
    if len(most_similar) == 3:
        print(f"If you liked Planet Hulk, we think you'll like {most_similar[0]}. Here's the plot:\n{most_similar[1]}")
    else:
        for i in range(0, len(most_similar), 3):
            movie_name = most_similar[i]
            movie_plot = most_similar[i+1]
            print(f"If you liked Planet Hulk, we think you'll like {movie_name}. Here's the plot:\n{movie_plot}")

recommended_movies()

# Host your solution on a Git host such as GitLab or GitHub.
# Remember to exclude any venv or virtualenv files from your repo.
# Add the link for your remote Git repo to your semantic_similarity.txt file.