# Day 7 - News Scraper

A Python-based automation tool to **scrape the latest headlines** from a news website.  
This is part of my **Python Automation Journey**.

---

## Features

-  Scrapes latest news headlines
-  Works with Inshorts or other news sites
-  Clean output with numbered headlines
-  Handles connection errors gracefully
-  Easy to extend to save or filter news

---

##  How It Works

- Uses `requests` to fetch web content
- Parses HTML using `BeautifulSoup`
- Extracts headlines from the news page
- Displays them in a clean, numbered list

---

## Usage
```bash
python news_scraper.py
```
---
## Output
```vbnet
📰 News Scraper - Top Headlines

1. India's economy expected to grow at 6.5% this year
2. NASA plans to send humans to Mars by 2040
3. New AI model breaks language translation records
...
```

## Flow
```pgsql
+----------------------------+
|        Start              |
+----------------------------+
             |
             v
+----------------------------+
| Set URL of News Website   |
+----------------------------+
             |
             v
+----------------------------+
| Send HTTP GET Request     |
+----------------------------+
             |
             v
+----------------------------+
| Is Response Successful?   |
+----------------------------+
        | Yes     | No
        v         v
+----------------+  +-------------------------+
| Parse HTML     |  | Print Error Message     |
| with BeautifulSoup |  +-------------------------+
+----------------+          |
        |                   v
        |           +-------------------------+
        |           | Return Empty List       |
        |           +-------------------------+
        v
+----------------------------+
| Extract Headlines (tags)   |
+----------------------------+
             |
             v
+----------------------------+
| Strip Text & Create List  |
+----------------------------+
             |
             v
+----------------------------+
| Is List Empty?            |
+----------------------------+
        | No      | Yes
        v         v
+----------------+  +-------------------------+
| Print Headlines|  | Print "No headlines"    |
| with numbering |  +-------------------------+
+----------------+
             |
             v
+----------------------------+
|           End              |
+----------------------------+
```

## ⚙️ Requirements

```bash
pip install requests beautifulsoup4

