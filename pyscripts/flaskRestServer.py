from flask import Flask, request, make_response
import requests, json

app = Flask(__name__)
url = 'https://postman-echo.com/post'

@app.route('/helloworld', methods=['GET','POST'])
def create_row_in_gs():
    if request.method == 'GET':
        return make_response('GET not implemented.')

    if request.method == 'POST':
        param = request.json['param']

        helloWorldMessage = "Hello " + str(param) + ", from Flask REST server!"
        create_row_data = {'passedInData': str(param)}

        response = requests.post(
            url, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )
        return helloWorldMessage + "\n" + str(response.content)

if __name__ == '__main__':
    app.run(host='localhost',debug=False, use_reloader=True)
