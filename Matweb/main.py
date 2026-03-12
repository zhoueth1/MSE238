import cloudscraper

def fetch_page(url):
  # Create scraper session
  scraper = cloudscraper.create_scraper(
    browser={
      "browser": "chrome",
      "platform": "windows",
      "mobile": False
    }
  )

  try:
    response = scraper.get(url, timeout=30)

    if response.status_code == 200:
      print("Success")
      return response.text
    else:
      print(f"Request failed: {response.status_code}")
      return None

  except Exception as e:
    print("Error:", e)
    return None


if __name__ == "__main__":
  url = "https://www.matweb.com/search/DataSheet.aspx?MatGUID="

  
  html = fetch_page(url)

  if html:
    print(html[:500])  # preview first 500 chars