from flask import Flask, url_for, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Don't look at this page"
    else:
        return request.get_data()

if __name__ == '__main__':
    app.run(debug=True)
