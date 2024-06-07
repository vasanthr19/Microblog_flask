from flask import Flask,render_template,request
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
  app=Flask(__name__)
  client=MongoClient(os.getenv("MONGODB_URI"))
  app.db=client.Microblog
  print('hello')
  entries=[]
  entries_with_date=[]
  @app.route('/',methods=['GET','POST'])
  def home():
    # ent=[e for e in app.db.entries.find()]
    entries_with_date=[]
    # print(ent)
    # entries_with_date=[(entry['content'],entry['date'],datetime.datetime.strptime(entry['date'],"%d-%m-%Y").strftime("%b %d"))
      # for entry in ent]
    # print('hi')
    # print([e for e in app.db.entries.find()])
    if request.method=='POST':
      entry_content=request.form.get("content")
      fmt_date=datetime.datetime.today().strftime("%d-%m-%Y")
      # entries.append((entry_content,fmt_date))
      app.db.entries.insert_one({'content':entry_content,'date':fmt_date})
      ent=[e for e in app.db.entries.find()]
      # print(ent)
      entries_with_date=[(entry['content'],entry['date'],datetime.datetime.strptime(entry['date'],"%d-%m-%Y").strftime("%b %d"))
      for entry in ent]
    return render_template("micro_home.html",entry=entries_with_date)
  return app

  # @app.route('/html')
  # def hel_html():
  #   return render_template("second_page.html")
      