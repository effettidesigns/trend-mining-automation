import os
import requests
from notion_client import Client
from bs4 import BeautifulSoup

# Configurazione Notion
notion = Client(auth=os.environ["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"])
DATABASE_ID = os.environ["1f3a908a809f80c3a9acfe3ed6e0cee9?v=1f3a908a809f81fc8470000c224ca709&pvs=4"]

# Funzione di scraping di esempio (Instagram hashtag)
def scrape_instagram_hashtag(sports):
    url = f"https://www.instagram.com/explore/tags/{sports}/"
    # ... scraping con requests + BeautifulSoup
    # return lista di dict: [{"trend": "...", "desc": "...", "link": "..."}]
    return [{"trend": "...", "desc": "...", "link": "..."}]

# Funzione per creare pagina in Notion
def push_to_notion(entry):
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties={
        "Trend Name": {"title":[{"text":{"content": entry["trend"]}}]},
        "Description": {"rich_text":[{"text":{"content": entry["desc"]}}]},
        "Link": {"url": entry["link"]},
        "Category": {"select": {"name": entry["category"]}},
        "Possible application": {"rich_text":[{"text":{"content": entry["application"]}}]},
        "Import date": {"date": {"start": entry["date"]}}
    })

if __name__ == "__main__":
    # Esempio: scrappo hashtag
    trends = scrape_instagram_hashtag("sportsdesign")
    for t in trends:
        push_to_notion(t)
