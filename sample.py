from flask import Flask
from flask import request, redirect
from flask_cors import CORS
from flask import request
import requests as req
import urllib2
from bs4 import BeautifulSoup, Tag
from pprint import pprint
import json
app = Flask(__name__)
CORS(app)

@app.route('/fetchNptel_metadata', methods=['GET'])
def fetchNpteldata():
   meta_data_list = []
   junk_data_list = []
   page = urllib2.urlopen('http://nptel.ac.in/syllabus/106102064/').read()
   soup = BeautifulSoup(page)
   for link in soup.find_all('a'):
      text = link.get_text()
      if(text == "Computer Science and  Engineering" or text == "Prof. Naveen Garg" or text == "Adobe Flash player"):
         meta_data_list.append(text)
      else:
         junk_data_list.append(text)

   with open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/nptel-metadata.json", "r") as jsonFile:
      data = json.load(jsonFile)
      
   data['course_name']= meta_data_list[0]
   data['faculty_name']= meta_data_list[1]
   data['prerequisites']= meta_data_list[2]

   with open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/nptel-metadata.json", "w") as jsonFile:
      json.dump(data, jsonFile)
   return redirect('/queryData')

@app.route('/queryData', methods=['GET'])
def queryData():
   searchfile = open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/vlabsmetadata.txt", "r")
   for line in searchfile:
      if "Computer" in line:
         print line
   searchfile.close()
   return "hello world"

if __name__ == '__main__':
   app.run(debug=True)
