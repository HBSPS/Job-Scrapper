# https://remoteok.io/remote-dev+python-jobs

# No page number

import requests
from bs4 import BeautifulSoup


def extract_job(html):
  title = html.find("td", {"class": "company"}).find("h2").get_text(strip=True)
  company = html.find("td", {"class": "company"}).find("h3").get_text(strip=True)

  location_1 = html.find("td", {"class": "company"}).find_all("div", {"class": "location"}) 
  if len(location_1) != 1:
    location = location_1[0].get_text(strip=True)
  else:
    location = None

  link_1= html.find("a", {"class": "preventLink"}).get('href')
  link = f"https://remoteok.com{link_1}"

  return {'title': title, 'company': company, 'location': location, 'link': link}


def extract_jobs(URL):
  jobs = []

  headers = { 'Accept-Language' : "en-US,en;q=0.9,ko;q=0.8",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
  result = requests.get(URL, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class":"job"})


  for result in results:
    job = extract_job(result)
    jobs.append(job)

  return jobs


#clear
def get_jobs_ro(word):
  URL = f"https://remoteok.io/remote-dev+{word}-jobs"

  jobs = extract_jobs(URL)

  return jobs