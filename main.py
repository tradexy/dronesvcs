import requests
from bs4 import BeautifulSoup

def check_url(url):
  try:
    r = requests.get(url)
    return r.status_code
  except:
    return None

def check_website_urls(website_url):
  r = requests.get(website_url)
  soup = BeautifulSoup(r.text, 'html.parser')

  broken_urls = []
  for link in soup.find_all('a'):
    url = link.get('href')
    status_code = check_url(url)
    if status_code == None:
      broken_urls.append(url)
    elif status_code >= 400:
      broken_urls.append(url)
  
  return broken_urls

website_url = "https://tradexy.github.io/dronesvcs/"
broken_urls = check_website_urls(website_url)
if len(broken_urls) > 0:
  print("The following URLs are broken:")
  for url in broken_urls:
    print(url)
else:
  print("No broken URLs were found.")
