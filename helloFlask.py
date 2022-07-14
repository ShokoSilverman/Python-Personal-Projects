from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/hello', methods = ['GET','POST'])
def helloIndex():
    word = request.args.get('word')
    return 'hello ' + word

@app.route('/testParam/<temp>')
def testParam(temp):
    return 'welcom %s' % temp

@app.route('/testQueryParams', methods=['POST'])
def test_query_params():
    args = request.args
    return args.to_dict()

@app.route('/nameTest', methods=['GET'])
def name_test():
    args = request.args
    fname = args.get('fname', default=None, type=str)
    lname = args.get('lname', default=None, type=str)
    if None not in (fname, lname):
        return f'hello {fname} {lname}!'
    elif fname is None and lname is None:
        return 'hello peter!'
    elif fname is None:
        return f'hello... {lname}???'
    else:
        return f'hello {fname}'
    
@app.route('/getJSON', methods=['GET'])
def test_json():
    json: dict = request.json
    return json


app.run(host='0.0.0.0', port=8080)