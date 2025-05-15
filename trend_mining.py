```python
import os
import requests
import feedparser
from notion_client import Client
from bs4 import BeautifulSoup
from datetime import datetime

# === Configurazione Notion ===
notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DB_ID"]

# === Funzioni di scraping ===

def scrape_instagram_hashtag(hashtag, limit=5):
    """
    Simula il recupero dei post top da un hashtag Instagram.
    """
    # Placeholder: integrazione reale richiederebbe API private o tool come Instaloader
    return [
        {
            "trend": f"#{hashtag} Top Post {i+1}",
            "desc": f"Caption esempio n.{i+1} per hashtag {hashtag}.",
            "link": f"https://www.instagram.com/p/EXAMPLE{i+1}",
            "category": "Visual Design",
            "application": "Ispirazione per layout di feed.",
            "date": datetime.now().isoformat()
        }
        for i in range(limit)
    ]


def scrape_tiktok_trending(limit=5):
    """
    Simula il recupero dei video di tendenza su TikTok.
    """
    return [
        {
            "trend": f"TikTok Trend Video {i+1}",
            "desc": "Stile video creativo con transizioni rapide.",
            "link": f"https://www.tiktok.com/@example/video/{1000+i+1}",
            "category": "Motion",
            "application": "Adattare per short reel.",
            "date": datetime.now().isoformat()
        }
        for i in range(limit)
    ]


def scrape_threads_trending(limit=5):
    """
    Placeholder per il fetch dei post più discussi su Threads.
    """
    return [
        {
            "trend": f"Threads Topic {i+1}",
            "desc": "Discussione su innovazione nel design sportivo.",
            "link": f"https://threads.net/t/EXAMPLE{i+1}",
            "category": "Discussion",
            "application": "Input per post di approfondimento.",
            "date": datetime.now().isoformat()
        }
        for i in range(limit)
    ]


def scrape_youtube_trends(channel_id, api_key, limit=5):
    """
    Usa YouTube Data API per ottenere i video recenti di un canale.
    Richiede YOUTUBE_API_KEY e channel_id.
    """
    url = (
        f"https://www.googleapis.com/youtube/v3/search?key={api_key}"
        f"&channelId={channel_id}&part=snippet&order=date&maxResults={limit}"
    )
    resp = requests.get(url).json()
    results = []
    for item in resp.get('items', []):
        title = item['snippet']['title']
        link = f"https://youtu.be/{item['id']['videoId']}"
        results.append({
            "trend": title,
            "desc": item['snippet']['description'],
            "link": link,
            "category": "Video Content",
            "application": "Storyboard per reel.",
            "date": item['snippet']['publishedAt']
        })
    return results


def scrape_rss_feed(feed_url, limit=5):
    """
    Estrapola gli ultimi articoli da un feed RSS.
    """
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries[:limit]:
        entries.append({
            "trend": entry.title,
            "desc": entry.get('summary', ''),
            "link": entry.link,
            "category": "Article",
            "application": "Insight per blog post o presentazioni.",
            "date": entry.published
        })
    return entries

# === Funzione per inviare i trend a Notion ===
def push_to_notion(entry):
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties={
        "Trend Name": {"title": [{"text": {"content": entry["trend"]}}]},
        "Descrizione sintetica": {"rich_text": [{"text": {"content": entry["desc"]}}]},
        "Fonti (Link)": {"url": entry["link"]},
        "Categoria": {"multi_select": [{"name": entry["category"]}]},
        "Applicazione possibile": {"rich_text": [{"text": {"content": entry["application"]}}]},
        "Data di raccolta": {"date": {"start": entry["date"]}}
    })

# === Main: raccolta e push settimanale ===
if __name__ == "__main__":
    all_trends = []
    # Instagram
    all_trends += scrape_instagram_hashtag("sportsdesign")
    # TikTok
    all_trends += scrape_tiktok_trending()
    # Threads
    all_trends += scrape_threads_trending()
    # YouTube (esempio con parametri)
    all_trends += scrape_youtube_trends(
        channel_id=os.environ.get("YOUTUBE_CHANNEL_ID", ""),
        api_key=os.environ.get("YOUTUBE_API_KEY", ""),
    )
    # Blog e magazine (RSS)
    feeds = [
        "https://www.creativebloq.com/feed",
        "https://medium.com/feed/tag/sports-design",
        # aggiungi altri feed RSS utili
    ]
    for feed in feeds:
        all_trends += scrape_rss_feed(feed)

    # Invia ogni trend a Notion
    for trend in all_trends:
        push_to_notion(trend)
```
