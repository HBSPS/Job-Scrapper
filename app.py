# """
# These are the URLs that will give you remote jobs for the word 'python'

# https://stackoverflow.com/jobs?r=true&q=python
# https://weworkremotely.com/remote-jobs/search?term=python
# https://remoteok.io/remote-dev+python-jobs

# Good luck!
# """

from flask import Flask, render_template, request, redirect, send_file
from SO_Scrapper import get_jobs_so
from RO_Scrapper import get_jobs_ro
from WWR_Scrapper import get_jobs_wwr
from exporter import save_to_file

app = Flask("Awesome Scrapper")

db_all = {}



@app.route("/")
def home():
  return render_template("home.html")


@app.route("/report")
def report():
  word = request.args.get('word')

  try:
    if word:
      word = word.lower()
      DB_jobs = db_all.get(word)

      if DB_jobs:
        jobs = DB_jobs
      else:
        jobs = get_jobs_all(word)
        db_all[word] = jobs
    else:
      redirect("/error")

    return render_template(
      "report.html",
      searchingBy_all=word,
      resultNumber_all = len(jobs),
      jobs = jobs
    )
  except:
    return redirect("/error")

  

  
@app.route("/export")
def export():
  try:
    word = request.args.get('word')

    if not word:
      raise Exception()

    word = word.lower()
    jobs = db_all.get(word)

    if not jobs:
      raise Exception()
      
    save_to_file(jobs, word)
    
    return send_file(
      f"{word}.csv",
      mimetype = "text/csv",
      as_attachment = True,
      attachment_filename = f"{word}.csv"
    )
  except:
    return redirect("/error")


@app.route("/error")
def error():
  return render_template("error.html")






def get_jobs_all(word):
  jobs_ro = get_jobs_ro(word)
  jobs_so = get_jobs_so(word)
  jobs_wwr = get_jobs_wwr(word)
  jobs = jobs_ro + jobs_so + jobs_wwr

  return jobs



# app.run(host = "0.0.0.0")