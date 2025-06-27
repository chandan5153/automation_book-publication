import os
import webbrowser

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: 'Georgia', serif; line-height: 1.6; margin: 40px; background-color: #fdfdfd; color: #222; }}
        h1 {{ color: #444; }}
        .chapter {{ white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="chapter">{content}</div>
</body>
</html>
"""

def generate_html(content, chapter_id, title="Chapter"):
    html = HTML_TEMPLATE.format(title=title, content=content)
    output_dir = "web_output"
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, f"{chapter_id}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Saved HTML: {html_path}")

    # Optional: open in browser
    webbrowser.open(f"file://{os.path.abspath(html_path)}")

    return html_path
