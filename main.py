from scraping.scraper import scrape_chapter
from ai_pipeline.ai_writer import ai_writer
from ai_pipeline.ai_reviewer import ai_reviewer
from ai_pipeline.human_loop_interface import human_review
from storage.versioning import save_version

def pipeline(url):
    raw = scrape_chapter(url)
    spun = ai_writer(raw)
    reviewed = ai_reviewer(spun)
    final = human_review(reviewed)
    save_version("chapter_1", final)
    print("\n✅ Final version saved.")

if __name__ == "__main__":
    pipeline("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
