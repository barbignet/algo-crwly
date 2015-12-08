import requests
import urlparse
from BeautifulSoup import BeautifulSoup
import tldextract
import Queue


# BFS Scanning depth
web_depth = 5

def queue_testing():
    q = Queue.Queue()

    for i in range(0,web_depth):
        q.put(('url', i))

    while not q.empty():
        print q.get()[1]



def print_webpage_links(url):

    urls = set()

    r = requests.get(url)
    # print r.status_code
    html_response = r.text

    soup = BeautifulSoup(html_response)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        curr_link = tag['href']

        if (tldextract.extract(curr_link).domain != tldextract.extract(url).domain):
            continue

        urls.add(curr_link)
        # print tag['href']
    print urls

#print_webpage_links('http://in.bgu.ac.il')
queue_testing()
