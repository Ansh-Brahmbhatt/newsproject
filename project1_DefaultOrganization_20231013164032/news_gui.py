'''
This file contains the NewsGUI class which handles the graphical user interface.
'''
import tkinter as tk
class NewsGUI:
    def __init__(self, top_news):
        self.top_news = top_news
    def start_gui(self):
        # Create the main window
        window = tk.Tk()
        window.title("Top 5 News")
        # Create a label for each news article
        for i, news in enumerate(self.top_news):
            label = tk.Label(window, text=f"{i+1}. {news['title']}")
            label.pack()
        # Start the GUI event loop
        window.mainloop()