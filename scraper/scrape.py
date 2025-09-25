import requests
from bs4 import BeautifulSoup
import argparse
import json
from pathlib import Path

# Import DB and models from app
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app import models

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_books(pages=1):
    results = []
    base = "http://books.toscrape.com/catalogue/page-{}.html"
    
    for page in range(1, pages + 1):
        url = base.format(page)
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print(f"⚠️ Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(r.text, "html.parser")

        for item in soup.select(".product_pod"):
            title = item.h3.a["title"]
            link = item.h3.a["href"]
            price = item.select_one(".price_color").text
            category = "Books"  # This site doesn’t expose category directly per book

            results.append({
                "title": title,
                "url": link,
                "category": category,
                "price_or_author": price
            })
    return results


def save_json(data):
    Path("samples").mkdir(exist_ok=True)
    with open("samples/scraped.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Saved {len(data)} records to samples/scraped.json")


def insert_db(data):
    from app.database import engine
    models.Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        try:
            for record in data:
                exists = db.query(models.ScrapedResource).filter_by(url=record["url"]).first()
                if not exists:
                    obj = models.ScrapedResource(
                        title=record["title"],
                        url=record["url"],
                        category=record["category"],
                        price_or_author=record["price_or_author"]
                    )
                    db.add(obj)
            db.commit()
            print(f"✅ Inserted {len(data)} rows into scraped_resources table")
        except Exception as e:
            db.rollback()
            import traceback; traceback.print_exc()
            print("❌ DB insertion failed:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--db", action="store_true", help="Insert into DB")
    args = parser.parse_args()

    data = scrape_books(args.pages)
    save_json(data)

    if args.db:
        insert_db(data)
