import os
import requests
from notion_client import Client
from bs4 import BeautifulSoup
from datetime import datetime

# Configurazione Notion
notion = Client(auth=os.environ["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"])
DATABASE_ID = os.environ["1f3a908a809f80c3a9acfe3ed6e0cee9?v=1f3a908a809f81fc8470000c224ca709&pvs=4"]

# Funzione di scraping di esempio (Instagram hashtag - NON funzionerà senza browser automation o API)
def scrape_instagram_hashtag(sportsdesign):
    # Instagram è molto protetto, quindi questo è solo un placeholder.
    # Se vuoi davvero fare scraping da Instagram, ti consiglio strumenti come Instaloader, Puppeteer o strumenti con proxy/IP rotation.
    
    # Qui invece, simuleremo dei trend fittizi
    trends = [
        {
            "trend": f"#{sportsdesign} graphics evolution",
            "desc": "New design trend spotted in sport visuals with high contrast typography.",
            "link": f"https://www.instagram.com/explore/tags/{sportsdesign}/",
            "category": "Visual Design",
            "application": "Could inspire typography direction for MotoGP assets.",
            "date": datetime.now().isoformat()
        },
        {
            "trend": f"{sportsdesign} meets AI",
            "desc": "AI tools now used to generate motion graphic templates in sports.",
            "link": "https://futuretools.io/",
            "category": "Tech + AI",
            "application": "Explore integration of Cavalry with AI-generated data viz.",
            "date": datetime.now().isoformat()
        }
    ]
    return trends

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
    trends = scrape_instagram_hashtag("sportsdesign")
    for t in trends:
        push_to_notion(t)
