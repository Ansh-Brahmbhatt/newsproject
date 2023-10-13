'''
This file contains the UserPreferences class which handles the user's preferences.
'''
class UserPreferences:
    def __init__(self):
        self.preferences = {}
    def get_preferences(self):
        # Get the user's preferences (e.g., country, category) through user input or any other means
        self.preferences['country'] = input("Enter your country: ")
        self.preferences['category'] = input("Enter your preferred news category: ")