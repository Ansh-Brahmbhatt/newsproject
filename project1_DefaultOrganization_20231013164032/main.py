'''
This is the main file of the website that gives the top 5 news of the day personalized to the user.
'''
import tkinter as tk
from news_api import NewsAPI
from user_preferences import UserPreferences
from news_gui import NewsGUI
def main():
    # Create an instance of the NewsAPI class
    news_api = NewsAPI()
    # Create an instance of the UserPreferences class
    user_preferences = UserPreferences()
    # Get the user's preferences
    user_preferences.get_preferences()
    # Get the top 5 news articles based on user preferences
    top_news = news_api.get_top_news(user_preferences.preferences)
    # Create an instance of the NewsGUI class
    news_gui = NewsGUI(top_news)
    # Start the GUI
    news_gui.start_gui()
if __name__ == "__main__":
    main()