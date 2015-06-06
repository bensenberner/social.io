from flask import Flask, url_for, request, render_template
from iodpython.iodindex import IODClient
import json

app = Flask(__name__)
client = IODClient("http://api.idolondemand.com/","d1a8fb96-f5be-482a-bd9d-c8e63d096338")
f = open('harry.txt', 'r')

@app.route('/senti', methods=['POST'])
def index():
    #r = client.post('analyzesentiment',{'text':str(request.get_data())})
    r = client.post('analyzesentiment',{'text':f.read()})
    myjson = r.json()
    friendly = False if myjson['aggregate']['score'] < 0 else True
    listOfTopics = getListOfTopics(myjson)
    return json.dumps({"friendly":friendly, "topics":listOfTopics})

def getListOfTopics(myjson):
    topics = []
    happyThoughts = myjson['positive']
    for thought in happyThoughts:
        topic = thought['topic']
        if topic is not None:
            topicBreakdown = topic.split(' ')
            if len(topicBreakdown) < 4:
                topics.append(topic)
    # Get them unique without using numpy bullshit
    topics = list(set(topics))
    return topics

if __name__ == '__main__':
    app.run(debug=True)
