import os
from xml.dom.minidom import Document
from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template
from pyfiles.models import model2
from pyfiles.modelChose import case

sent = ''


# //////////////////////>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('info.html')


@app.route('/sumry', methods=['POST'])
def sumry():
    data = request.get_json()
    DOCUMENT = data['doc']
    firstLen = len(DOCUMENT.split())
    rat = data['ratio']
    modl = data['model']

    choose = case(modl)
    ret_sent = choose.choose(DOCUMENT, rat)
#  onno model er sob method eki rokom nao hote pare
# taiiii beware!!!!!!!!!!!!!

    response = jsonify(
        {
            "model-used": "{}".format(modl),
            'Compression': "{}/{}".format(
                sum([len(x.split()) for x in ret_sent]),
                firstLen),

            "Summery": ret_sent
        })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/<name>')
def name(name):
    return '''
    <div style="text-align: center;">
    <h2 style="display:block">Hello <h1 style="">{}!</h1></h2>
       <p> here are some instructions .........</br>
        1.get the browser open and install the postMan request plugin-CHrome</br>
        2. go to the link below and make a post request</br>
        3. make sure that the request body is in json format</br>
        4. ex: =>> "doc":"YOUR sent............","ratio":sent_number_in _intger </p>
         </div>
        '''.format(name)


@app.route('/instruct')
def instruct():
    return render_template('insruct.html')


@app.route('/info')
def render():
    return render_template('info.html')


@app.route('/sumup')
def sumup():
    return render_template('sumup.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
