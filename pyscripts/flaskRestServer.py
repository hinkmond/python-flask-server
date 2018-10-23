from flask import Flask, request, make_response
import requests, json

app = Flask(__name__)

@app.route('/helloworld', methods=['GET','POST'])
def create_row_in_gs():
    if request.method == 'GET':
        return make_response('GET not implemented.')

    if request.method == 'POST':
        param = request.json['param']

        helloWorldMessage = "Hello " + str(param) + ", from Flask REST server!"

        url = 'https://postman-echo.com/post'
        cookieDict = dict(cookieName="ABCDEFXYZ")
        jsonBody = {'passedInData': str(param)}

        response = requests.post(
            url, cookies=cookieDict, data=json.dumps(jsonBody),
            headers={'Content-Type': 'application/json'}
        )
        return helloWorldMessage + "\n" + str(response.content)

if __name__ == '__main__':
    app.run(host='localhost',debug=False, use_reloader=True)
