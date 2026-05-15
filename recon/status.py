import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def check_status(url):
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5,
            verify=False,
            allow_redirects=True
        )
  
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "NO TITLE"
        )

        return {
            "url": url,
            "status": response.status_code,
            "length": len(response.text),
            "title": title
        }

    except requests.RequestException:
        return None
        
    
