from flask import Flask
from flask import request
from flask_cors import CORS
from flask import request
import requests as req
import urllib2
from bs4 import BeautifulSoup, Tag
from pprint import pprint
import json
app = Flask(__name__)
CORS(app)

@app.route('/fetchMetadata', methods=['GET'])
def fetchData():
   meta_data_list = []
   junk_data_list = []
   page = urllib2.urlopen('http://nptel.ac.in/syllabus/106102064/').read()
   soup = BeautifulSoup(page)
   # data = {
   #    # 'course_name' : "",
   #    # 'shares' : 100,
   #    # 'price' : 542.23
   # }
   # json_str = json.dumps(data)
   # data = json.loads(json_str)
   
   for link in soup.find_all('a'):
      text = link.get_text()
      if(text == "Computer Science and  Engineering" or text == "Prof. Naveen Garg" or text == "Adobe Flash player"):
         meta_data_list.append(text)
      else:
         junk_data_list.append(text)

   with open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/metadata.json", "r") as jsonFile:
      data = json.load(jsonFile)

   #tmp = data["course_name"]
   data['course_name']= meta_data_list[0]

   with open("/home/sadhana/renarration_project/link-nptel-to-vlabs/v2.1_nptel_linking/metadata.json", "w") as jsonFile:
      json.dump(data, jsonFile)
   #f = open("/home/sadhana/renarration_project/link-nptel-to-vlabs/BM/metadata.json", "r")
   #json_obj = json.load(f)  # <--- this is a dictionary!
   #json_obj['metadata'] ={"name":"dsdas"}

   #data['name'].append("hello") 
   #meta_data = json.loads(open('/home/sadhana/renarration_project/link-nptel-to-vlabs/BM/metadata.json', 'r').read())
   #meta_data['course_name'] = "hello"
   
   #meta_data[course_name] = meta_data_list[0]
   #with open('metadata.json', 'w') as f:
    # json.dump(data, f)
   # filename = metadata['course_name']
   # file = open(filename, 'w')
   # try:
   #    file.write(sectioncontent)
   #    file.close()
   #    break	
   # except
   # Exception as e:
   # print str(e)
   return "hello"
   
if __name__ == '__main__':
   app.run(debug=True)
