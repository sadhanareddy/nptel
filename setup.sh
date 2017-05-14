#! bash script for setting up enviornment for web services

sudo apt-get install python-virtualenv

virtualenv flask

flask/bin/pip install flask

flask/bin/pip install conf

flask/bin/pip install -U flask-cors

flask/bin/pip install requests

flask/bin/pip install  beautifulsoup4

flask/bin/pip install  jsonify

#flask/bin/pip install urllib2