# ChatDev User Manual

## Introduction

Welcome to the ChatDev User Manual! This manual will guide you on how to use the website developed by ChatDev that gives you the top 5 news of the day personalized to you. This website is built using Python programming language and utilizes various dependencies to fetch news articles and create a graphical user interface.

## Installation

To use the website, you need to install the required dependencies. Follow the steps below to install the necessary dependencies:

1. Make sure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

2. Open a terminal or command prompt.

3. Navigate to the directory where you have downloaded the project files.

4. Run the following command to install the dependencies:

   ```
   pip install -r requirements.txt
   ```

   This command will install the required dependencies, including the `requests` library and `tkinter` module.

## Usage

Once you have installed the dependencies, you can use the website to get personalized news articles. Follow the steps below to use the website:

1. Open a terminal or command prompt.

2. Navigate to the directory where you have downloaded the project files.

3. Run the following command to start the website:

   ```
   python main.py
   ```

4. The website will prompt you to enter your country and preferred news category. Enter the requested information and press Enter.

5. The website will fetch the top 5 news articles based on your preferences and display them in a graphical user interface.

6. You can click on each news article to view more details or perform any desired actions.

7. To exit the website, close the graphical user interface window.

## Customization

If you want to customize the website or add additional features, you can modify the code in the project files. Here are some areas you can consider customizing:

- `user_preferences.py`: You can modify the `get_preferences` method to collect user preferences in a different way or add more preferences.

- `news_api.py`: You can modify the `get_top_news` method to fetch news articles from a different API or apply additional filters.

- `news_gui.py`: You can modify the graphical user interface to change the layout, styling, or add more interactive elements.

## Conclusion

Congratulations! You have successfully learned how to use the website developed by ChatDev to get personalized news articles. If you have any further questions or need assistance, please don't hesitate to reach out to our support team. Happy reading!