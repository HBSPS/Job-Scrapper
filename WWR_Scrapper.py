# https://weworkremotely.com/remote-jobs/search?term=python

import requests
from bs4 import BeautifulSoup


def get_sections(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  sections = soup.find_all("section", {"class": "jobs"})
  
  return sections


def extract_job_with_category(html, category):
  title = html.find("span", {"class": "title"}).string
  company = html.find("span", {"class": "company"}).string
  try:
    location = html.find("span", {"class": "region"}).string
  except:
    location = None
  link_1 = html.find_all("a")
  link = f"https://weworkremotely.com{link_1[1].get('href')}"


  return {'category': category, 'title': title, 'company': company, 'location': location, 'link': link}


def extract_job(html):
  title = html.find("span", {"class": "title"}).string
  company = html.find("span", {"class": "company"}).string
  try:
    location = html.find("span", {"class": "region"}).string
  except:
    location = None
  link_1 = html.find_all("a")
  link = f"https://weworkremotely.com{link_1[1].get('href')}"


  return {'title': title, 'company': company, 'location': location, 'link': link}


def extract_jobs(sections, URL):
  jobs = []

  for page in sections:
    results = page.find_all("li")
    del results[-1]

    #print(f"\n[{category}]")

    for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs



def get_jobs_wwr(word):
  URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"


  sections = get_sections(URL)

  jobs = extract_jobs(sections, URL)

  return jobs



#def get_jobs_wwr_category(word):

#  category = page.find("h2").find("a").string
  
#  for result in results:
#    job = extract_job_with_category(result, category)
#    jobs_with_category.append(job)