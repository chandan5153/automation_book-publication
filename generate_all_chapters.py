
import json
from scraping.scraper import scrape_chapter
from ai_pipeline.ai_writer import ai_writer

urls = [
    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1",
    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_2",
    "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_3",
]

all_data = []

for i, url in enumerate(urls, start=1):
    print(f"🔄 Fetching Chapter {i}")
    original = scrape_chapter(url)
    spun = ai_writer(original)

    all_data.append({
        "chapter": f"Chapter {i}",
        "url": url,
        "original": original,
        "spun": spun
    })

with open("web_output/chapters.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)

print("✅ chapters.json file created with 3 chapters!")
