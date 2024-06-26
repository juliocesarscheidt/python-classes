# import time
import requests
import concurrent.futures
from threading import current_thread

def get_wiki_page_existence(wiki_page_url, timeout=10):
  response = requests.get(url=wiki_page_url, timeout=timeout)
  print('thread id', current_thread().ident)
  # time.sleep(10)

  page_status = "UNKNOWN"
  if response.status_code == 200:
      page_status = "OK"
  elif response.status_code == 404:
      page_status = "NOT_FOUND"
  
  print(response.text[0:10])

  return wiki_page_url + " - " + page_status

wiki_page_urls = [
  "https://en.wikipedia.org/wiki/Ocean",
  "https://en.wikipedia.org/wiki/Island",
  "https://en.wikipedia.org/wiki/this_page_does_not_exist",
  "https://en.wikipedia.org/wiki/Shark",
]

with concurrent.futures.ThreadPoolExecutor() as executor:
  futures = []
  
  for url in wiki_page_urls:
    futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))

  for future in concurrent.futures.as_completed(futures):
    print(future.result())
