from flask import Flask, url_for, request, render_template
from iodpython.iodindex import IODClient
import json
import time
import operator
import numpy as np
from collections import OrderedDict

app = Flask(__name__)
client = IODClient("http://api.idolondemand.com/","d1a8fb96-f5be-482a-bd9d-c8e63d096338")

#f = open('cameron.txt', 'r')

@app.route('/senti', methods=['POST'])
def sentiment():
    if (request.get_data() == "Shubham Sharma"):
        with open('js/anthony.js') as data_file:
            data=json.load(data_file)
    elif (request.get_data() == "Lukas Bernreiter"):
        with open('js/doan.js') as data_file:
            data=json.load(data_file)
    elif (request.get_data() == "Thanh Le"):
        with open('js/cameron.js') as data_file:
            data=json.load(data_file)
    elif (request.get_data() == "Tanguy Abel"):
        with open('js/olivia.js') as data_file:
            data=json.load(data_file)
    elif (request.get_data() == "Jimmy Yeh"):
        with open('js/phil.js') as data_file:
            data=json.load(data_file)
    else:
        with open('js/help.js') as data_file:
            data=json.load(data_file)
    time.sleep(1)
    #r = client.post('analyzesentiment',{'text':str(request.get_data())})
    #r = client.post('analyzesentiment',{'text':f.read()})
    #myjson = r.json()
    #sentiment = myjson['aggregate']['sentiment']
    #listOfTopics = getListOfTopics(myjson)
    #sentiment = data['sentiment']
    #listOfTopics = data['topics']
    #return json.dumps({"sentiment":sentiment, "topics":listOfTopics})
    #return json.dumps(myjson)
    return json.dumps(data)

@app.route('/concept', methods=['POST'])
def concept():
    #r = client.post('extractconcepts',{'text':str(request.get_data()))
    r = client.post('extractconcepts',{'text':f.read()})
    myjson = r.json()
    concepts = myjson['concepts']
    sorted_concepts = sorted(concepts, key=operator.itemgetter('occurrences'))
    sorted_concepts.reverse()
    #TODO: only return the top 10 concepts (sorted_concepts[:10])
    return json.dumps(sorted_concepts)

def getListOfTopics(myjson):
    happyThoughts = sorted(myjson['positive'], key=operator.itemgetter('score'))
    topics = []
    for thought in happyThoughts:
        topic = thought['topic']
        if topic is not None:
            topicBreakdown = topic.split(' ')
            if len(topicBreakdown) < 4:
                topics.append(topic)
    # Get them unique without using numpy bullshit
    topics = list(OrderedDict.fromkeys(topics))
    return topics

if __name__ == '__main__':
    app.run(debug=True)
