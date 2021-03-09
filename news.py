# news api key c9f1e74bad9c4d15987647a248910093
import requests


from pprint import pprint

class NewsFeed:
    base_url = "http://newsapi.org/v2/everything?"
    api_key = "c9f1e74bad9c4d15987647a248910093"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language





    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''

        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2021-03-02', to_date='2021-12-02', language='en')
    print(news_feed.get())






