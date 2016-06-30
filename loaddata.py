"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K15.
"""

# imports
import os
import json
import pprint

# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
META_DIR = os.path.join(DATA_DIR, 'metacritic')


def load_mojo_data():
    file_contents = os.listdir(MOJO_DIR)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(MOJO_DIR, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list

def load_metacritic_data():
    file_contents = os.listdir(META_DIR)

    meta_list = []

    for filename in file_contents:
        filepath = os.path.join(META_DIR, filename)

        with open(filepath, 'r') as meta_file:
            meta_data = json.load(meta_file)

        if isinstance(meta_data, dict):
            for k, v in meta_data.iteritems():
                if isinstance(v, list):
                    meta_data[k]=', '.join(map(str, v))
            meta_list.append(meta_data)
    print "Parsed %i metacritic files from %i files" % (len(meta_list), len(file_contents))

    return meta_list


if __name__ == "__main__":
    movies = load_mojo_data()
    meta = load_metacritic_data()
