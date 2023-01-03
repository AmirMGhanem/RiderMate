from flask import Flask
from utils.helpers import custom_response
from requests import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return custom_response({"hello world":"hahah"}, 200)



app.route('/api/v1/pingloc', methods=['POST'])
def pingloc():
    data = request.get_json()
    location = data['location']


if __name__ == '__main__':
    app.run()