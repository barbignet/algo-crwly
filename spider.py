import requests
import urlparse
from BeautifulSoup import BeautifulSoup

def print_webpage_links(url):
    r = requests.get(url)
    # print r.status_code
    html_response = r.text

    soup = BeautifulSoup(html_response)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        print tag['href']

print_webpage_links('http://in.bgu.ac.il')
