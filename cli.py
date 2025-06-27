import argparse
from scraping.scraper import scrape_chapter
from ai_pipeline.ai_writer import ai_writer
from ai_pipeline.ai_reviewer import ai_reviewer
from ai_pipeline.human_loop_interface import human_review_loop
from storage.versioning import save_version
import os

TMP_FILE = "output/working_draft.txt"

os.makedirs("output", exist_ok=True)

def write_tmp(content):
    with open(TMP_FILE, "w", encoding="utf-8") as f:
        f.write(content)

def read_tmp():
    with open(TMP_FILE, "r", encoding="utf-8") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Book Publication CLI Tool")
    parser.add_argument("step", choices=[
    "scrape", "write", "review", "human_loop", "save", "full_pipeline", "render_html"
])
    parser.add_argument("--url", type=str, help="URL to scrape")
    parser.add_argument("--id", type=str, default="chapter_1", help="Document ID")

    args = parser.parse_args()

    if args.step == "scrape":
        if not args.url:
            print("❌ Please provide --url to scrape.")
            return
        content = scrape_chapter(args.url)
        write_tmp(content)
        print("✅ Scraping complete and saved to draft.")
    elif args.step == "render_html":
        from generate_html import generate_html
        content = read_tmp()
        chapter_id = args.id or "chapter_1"
        generate_html(content, chapter_id, title=f"The Gates of Morning — {chapter_id.title()}")

    elif args.step == "write":
        raw = read_tmp()
        spun = ai_writer(raw)
        write_tmp(spun)
        print("✅ AI Writer output saved.")

    elif args.step == "review":
        spun = read_tmp()
        reviewed = ai_reviewer(spun)
        write_tmp(reviewed)
        print("✅ AI Reviewer output saved.")

    elif args.step == "human_loop":
        reviewed = read_tmp()
        final = human_review_loop(reviewed)
        write_tmp(final)
        print("✅ Final human-approved draft saved.")

    elif args.step == "save":
        final = read_tmp()
        save_version(args.id, final)
        print("✅ Version saved to ChromaDB.")

    elif args.step == "full_pipeline":
        if not args.url:
            print("❌ Please provide --url to scrape.")
            return
        raw = scrape_chapter(args.url)
        spun = ai_writer(raw)
        reviewed = ai_reviewer(spun)
        final = human_review_loop(reviewed)
        save_version(args.id, final)
        print("✅ Full pipeline completed and version saved.")

if __name__ == "__main__":
    main()
