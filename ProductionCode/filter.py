"""
filter.py

This module provides the Filter class for filtering media entries such as movies and TV shows.
Filters can be applied based on actor names, genres/categories, and release years. The class
operates on a dictionary of media objects and supports retrieving and printing the filtered results.
"""
import re
from ProductionCode import data

dataset = data.Data()

def filter_dataset(name, category, year):
    """
    Filters the dataset based on all the parameters provided by a user 
    and returns the results as a string.
    """
    dataset_filter = Filter()

    filter_types = [dataset_filter.filter_by_actor, dataset_filter.filter_by_category,
                    dataset_filter.filter_by_year_onward]
    user_inputs = [name, category, year]
    for filter_type, user_input in enumerate(user_inputs):
        if _is_not_empty(user_input):
            user_input = _insert_spaces(user_input)
            filter_types[filter_type](user_input)
    return dataset_filter.get_filtered_titles_string()

def _is_not_empty(search_term):
    """
    Checks whether an input parameter is not unused/"empty."
    """
    if search_term in {"_", "-", "x"}:
        return False
    return True

def _insert_spaces(search_string):
    """
    Ensures that input parameters contain spaces where necessary.
    """
    search_string = re.sub(r"%20|-|_", " ", search_string)
    return search_string.lower()

class Filter:
    """
    Class with functions to easily filter movies based on actor, genre, and year.
    """

    def __init__(self):
        """
        Initializes the Filter with data from the dataset and creates a copy to be filtered.
        """
        self.media_dict = dataset.get_media_dict()
        self.filtered_media_dict = self.media_dict.copy()

    def filter_by_actor(self, name):
        """
        Filters the media to only include entries featuring the specified actor.
        """
        for title in self.filtered_media_dict.copy():
            cast = self.filtered_media_dict[title].cast
            if name.lower() not in (actor.lower() for actor in cast):
                del self.filtered_media_dict[title]

    def filter_by_category(self, category):
        """
        Filters the media to only include entries that belong to the specified genre/category.
        """
        for title in self.filtered_media_dict.copy():
            categories = self.filtered_media_dict[title].listed_in
            if category.lower() not in (cat.lower() for cat in categories):
                del self.filtered_media_dict[title]

    def filter_by_year_onward(self, year):
        """
        Filters the media to only include entries released in or after the specified year.
        """
        for title in self.filtered_media_dict.copy():
            release_year = self.filtered_media_dict[title].release_year
            if int(year) > int(release_year):
                del self.filtered_media_dict[title]

    def get_filtered_titles_string(self):
        """
        Returns a string containing the titles of the media entries after filtering.
        """
        titles = ""
        for media in self.filtered_media_dict.values():
            titles += f"{media.title}</br>"
        return titles

    def print_filtered_all(self):
        """
        Prints all available details of each media entry in the filtered dictionary.
        """
        for media in self.filtered_media_dict.values():
            print(f"Title: {media.title}")
            print(f"Show ID: {media.show_id}")
            print(f"Media Type: {media.media_type}")
            print(f"Director: {media.director}")
            print(f"Cast: {media.cast}")
            print(f"Country: {media.country}")
            print(f"Date Added: {media.date_added}")
            print(f"Release Year: {media.release_year}")
            print(f"Rating: {media.rating}")
            print(f"Duration: {media.duration}")
            print(f"Listed In: {media.listed_in}")
            print(f"Description: {media.description}")
            print(f"Streaming Services: {media.streaming_service}\n")
