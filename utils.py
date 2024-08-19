import os
import requests
from bs4 import BeautifulSoup

required_keys = ['url', 'api_token']

## stripe_fintech_policy = 'https://stripe.com/docs/treasury/marketing-treasury'

def validate_request_data(request_json):
    for k in required_keys:
        if k not in request_json:
            return False
    return True

def sanitize_url(url):
    u = url.replace('https://', '')
    u = u.replace('http://', '')
    return u.replace('/', '-')

## handle exceptions gracefully here
def load_website_content(target_url):
    response = requests.get(target_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content = soup.get_text(separator='\n', strip=True)
    return text_content

