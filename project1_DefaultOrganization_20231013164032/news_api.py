import requests

class NewsAPI:
    def __init__(self):
        self.api_key = "a72cef5123144e97ac6aa7c7be57dc21"  # Replace with your actual API key
    
    def get_top_news(self, preferences):
        # Make a request to the news API to get the top news articles
        url = f"https://newsapi.org/v2/top-headlines?country={preferences['country']}&category={preferences['category']}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        # Extract the top 5 news articles
        top_news = data['articles'][:5]
        return top_news


