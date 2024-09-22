import requests
from bs4 import BeautifulSoup

def get_medicines(medicine_name):
    # Example: Using a hypothetical online pharmacy
    url = f"https://example-pharmacy.com/search?q={medicine_name}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    names = [item.text for item in soup.select('.medicine-name')]
    prices = [item.text for item in soup.select('.medicine-price')]
    order_links = [item['href'] for item in soup.select('.order-link')]
    
    return {
        'names': names,
        'prices': prices,
        'order_links': order_links
    }
