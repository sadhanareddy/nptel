from flask import Flask
from flask import request, redirect
from flask_cors import CORS
from flask import request
import requests as req
import urllib2
from bs4 import BeautifulSoup, Tag
import json
from flask import jsonify
app = Flask(__name__)
CORS(app)

@app.route('/fetchNptel_metadata', methods=['GET'])
def fetchNpteldata():
   page = urllib2.urlopen('http://nptel.ac.in/courses/106102064/').read()
   soup = BeautifulSoup(page)
   # kill all script and style elements
   for script in soup(["script", "style"]):
       script.extract()    # rip it out
   text = soup.get_text()
   # break into lines and remove leading and trailing space on each
   lines = (line.strip() for line in text.splitlines())
   # break multi-headlines into a line each
   chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
   # drop blank lines
   text = '\n'.join(chunk for chunk in chunks if chunk)
   #print text
   global keywords
   keywords = text.split()
   keywords = list(set(keywords))
   #print keywords
   #return "hello world"
   return redirect('/queryData')

@app.route('/queryData', methods=['GET'])
def queryData():
   # data = []
   # for word in keywords:
   #     searchfile = open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/vlabsmetadata.txt", "r")
   #     for line in searchfile:
   #         if word in line:
   #             data.append(line)
   #             print data
   #             #print str(line)
   # searchfile.close()
   #return jsonify(results = data)
   return "hi....."

if __name__ == '__main__':
   app.run(debug=True)
