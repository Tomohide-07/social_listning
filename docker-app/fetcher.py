import pandas as pd
import snscrape.modules.twitter as sntwitter
from utils import clean_text


def fetch_posts(keyword: str, limit: int = 100) -> pd.DataFrame:
    """
    Fetch recent Tweets matching the keyword, clean and anonymize.
    """
    posts = []
    query = f"{keyword} lang:en"
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        posts.append(clean_text(tweet.content))
    return pd.DataFrame(posts, columns=["text"])