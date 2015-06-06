from flask import Flask, url_for, request
from iodpython.iodindex import IODClient
import json

app = Flask(__name__)
client = IODClient("http://api.idolondemand.com", "d1a8fb96-f5be-482a-bd9d-c8e63d096338")

f = open('harry.txt', 'r')
words = f.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        r = client.post('analyzesentiment',{'text':'Your mother is a whore'})
        return r
    else:
        return "fluck you"
        #return request.get_data()


if __name__ == '__main__':
    app.run(debug=True)
