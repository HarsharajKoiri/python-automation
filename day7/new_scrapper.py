import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Scraping headlines from Inshorts
        headlines = soup.find_all('span', itemprop='headline')

        if not headlines:
            print("No headlines found. Try a different site structure.")
            return []

        return [headline.get_text(strip=True) for headline in headlines]

    except requests.exceptions.RequestException as e:
        print("Error fetching the website:", e)
        return []

# Main Program
if __name__ == "__main__":
    print("📰 News Scraper - Top Headlines\n")
    url = "https://inshorts.com/en/read"  # You can try other news websites too

    headlines = fetch_headlines(url)

    if headlines:
        for i, h in enumerate(headlines, 1):
            print(f"{i}. {h}")
    else:
        print("No headlines to display.")
