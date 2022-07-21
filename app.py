import os
from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


sent = ''


def cleanText(text):

    text = re.sub(r'\n|\r', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    sent = text.split('।')
    sent2 = text.split('.')

    if len(sent) < len(sent2):
        sent = sent2[:-1]

    return sent


def tokner(str):
    return str.split()


def getSimmat(sent):
    vectorizer = TfidfVectorizer(tokenizer=tokner)
    vectors = vectorizer.fit_transform(sent)
    dt_matrix = vectors.toarray()

    similarity_matrix = np.matmul(dt_matrix, dt_matrix.T)
    return similarity_matrix


def run_page_rank(similarity_matrix):

    # constants
    damping = 0.85  # damping coefficient, usually is .85
    min_diff = 1e-5  # convergence threshold
    steps = 100  # iteration steps

    pr_vector = np.array([1] * len(similarity_matrix))

    # Iteration
    previous_pr = 0
    for epoch in range(steps):
        pr_vector = (1 - damping) + damping * \
            np.matmul(similarity_matrix, pr_vector)
        # print(pr_vector)
        if abs(previous_pr - sum(pr_vector)) < min_diff:
            break
        else:
            previous_pr = sum(pr_vector)

    return pr_vector


def get_top_sentences(pr_vector, sentences, number):

    top_sentences = []

    if pr_vector is not None:

        sorted_pr = np.argsort(pr_vector)
        # print(sorted_pr)
        sorted_pr = list(sorted_pr)
        # it means from big to small... the upper thing was for small to big >>  ascending...............
        sorted_pr.reverse()
        # print(sorted_pr)
        sorted_pr = sorted_pr[:10]
        # print(sorted_pr)
        index = 0
        sorted_pr.sort()
        # print(sorted_pr)
        for epoch in range(number):
            sent = sentences[sorted_pr[index]]
            # sent = normalize_whitespace(sent)
            top_sentences.append(sent)
            index += 1

    return top_sentences


# //////////////////////>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('info.html')


@app.route('/sumry', methods=['POST'])
@cross_origin()
def sumry():
    data = request.get_json()
    DOCUMENT = data['doc']
    rat = data['ratio']
    DOCUMENT = cleanText(DOCUMENT)
    print(DOCUMENT)
    similarity_matrix = getSimmat(DOCUMENT)

    scores = run_page_rank(similarity_matrix)

    ret_sent = get_top_sentences(scores, DOCUMENT, int(rat))
    print(ret_sent)
    # resl= (summarize(DOCUMENT, ratio=rat, split=False))

    response = jsonify(
        {'LENGTH': sum([len(x.split()) for x in ret_sent]), "Summery": ret_sent})
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
