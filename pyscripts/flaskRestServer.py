from flask import Flask, request, make_response
from flask_cors import cross_origin
import requests, json


app = Flask(__name__)

@app.route('/helloworld', methods=['GET','POST'])
@cross_origin()  # Make this endpoint able to be called from cross-origins
def showHelloWorldExample():
    """
    POST endpoint that shows hello world message with data (response) from a nested REST POST
      call to the URL: https://postman-echo.com/post inside this endpoint function

    :param @app.route(...) See: Python package "requests"
    :return: { parameter :  value from procedure }

    Example usage:
    $ curl -X POST -H "Content-Type:application/json" http://localhost:5000/helloworld -d '{"param": "World"}'

    Hello World, from Flask REST server!
    Here is the REST POST response content from postman-echo.com b'{"args":{},"data":{"passedInData":"World"},
    "files":{},"form":{},"headers":{"x-forwarded-proto":"https","host":"postman-echo.com","content-length":"25",
    "accept":"*/*","accept-encoding":"gzip, deflate","content-type":"application/json","cookie":"cookieName=ABCDEFXYZ",
    "user-agent":"python-requests/2.19.1","x-forwarded-port":"443"},"json":{"passedInData":"World"},
    "url":"https://postman-echo.com/post"}'
    """
    if request.method == 'GET':
        return make_response('GET not implemented.')

    if request.method == 'POST':

        # Keep track of the passed in data body parameter called param.  Ex. '{"param": "myValue"}'
        #   Use this for the Hello World message that is returned in thr response.
        param = request.json['param']

        # Make an embedded REST POST call to the postman-echo.com endpoint named /post
        url = 'https://postman-echo.com/post'
        cookieDict = dict(cookieName="ABCDEFXYZ")
        jsonBody = {'passedInData': str(param)}
        response = requests.post(
            url, cookies=cookieDict, data=json.dumps(jsonBody),
            headers={'Content-Type': 'application/json'}
        )

        # Return a combination of the Hello World message with the passed in "param", and the response from
        #   postman-echo.com
        helloWorldMessage = "\nHello " + str(param) + ", from Flask REST server!\n\n"
        return helloWorldMessage + "Here is the REST POST response content from postman-echo.com:\n===\n" + \
               str(response.content) + "\n"

if __name__ == '__main__':
    app.run(host='localhost',debug=False, use_reloader=True)
