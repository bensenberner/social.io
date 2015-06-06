from iodpython.iodindex import IODClient
client = IODClient("http://api.idolondemand.com/","d1a8fb96-f5be-482a-bd9d-c8e63d096338")
r = client.post('analyzesentiment',{'text':'I like cat'})
myjson = r.json()
print myjson
