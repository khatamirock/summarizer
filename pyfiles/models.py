import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# for model-1
import pandas as pd
import re
# from nltk.tokenize import sent_tokenize
# from nltk.corpus import stopwords
# from gensim.models import Word2Vec

from scipy import spatial
# import networkx as nx
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')


def tokner(str):
    return str.split()


class model2:

    def cleanText(self, text):

        text = re.sub(r'\n|\r', ' ', text)
        text = re.sub(r' +', ' ', text)
        text = text.strip()
        sent = text.split('।')

        sent2 = text.split('.')

        if len(sent) < len(sent2):
            sent = sent2[:-1]

        return sent

    def getSimmat(self, sent):
        vectorizer = TfidfVectorizer(tokenizer=tokner)
        vectors = vectorizer.fit_transform(sent)
        dt_matrix = vectors.toarray()

        similarity_matrix = np.matmul(dt_matrix, dt_matrix.T)
        return similarity_matrix

    def run_page_rank(self, similarity_matrix):

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

    def get_top_sentences(self, pr_vector, sentences, number):

        top_sentences = ''

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
                top_sentences += sent
                index += 1

        return top_sentences


# # with word embedding and nx
# class model1:
#     sentences_clean = ''
#     sentences = ''
#     def embed(self, text):

#         global sentences_clean
#         global sentences
#         sentences = text.split('।')
#         if len(text.split('.')) > len(sentences):
#             sentences = text.split('.')

#         sentence_tokens = [
#             [words for words in sentence.split(' ')] for sentence in sentences]
#         sentences_clean = sentences
#         # print(sentences_clean)
#         max_len = max([len(tokens) for tokens in sentence_tokens])
#         w2v = Word2Vec(sentence_tokens, size=1, min_count=1, iter=1000)
#         # print(w2v['Classification'][0])
#         sentence_embeddings = [[w2v[word][0]
#                                 for word in words] for words in sentence_tokens]
#         sentence_embeddings = [np.pad(
#             embedding, (0, max_len-len(embedding)), 'constant') for embedding in sentence_embeddings]
#         ##    max_len- current_len

#         return sentence_embeddings

#     def one_to_other_simMat(self, target, sentence_embeddings):
#         targ = sentences_clean[target]
#         # print(targ)
#         i = 0
#         ar_lin = []
#         for x in sentence_embeddings:
#             # print('>>> ',sentences_clean[i])
#             i += 1
#             man = 1-spatial.distance.cosine(x, sentence_embeddings[target])
#             #                            current-sent_embedd, passde_val-of_target_embed
#             # print(man)
#             ar_lin.append(man)
#         return ar_lin

#     def getSimMat(self, text):
#         sentence_embeds = self.embed(text)

#         sim_mat = []

#         for x in range(len(sentences_clean)):
#             xx = self.one_to_other_simMat(x, sentence_embeds)
#             sim_mat.append(xx)
#             # print(xx)

#         sims = np.array(sim_mat)
#         return sims

#     # making pageRank in the graph method.........
#     def pageRank(self, sims):
#         nx_graph = nx.from_numpy_array(sims)
#         scores = nx.pagerank(nx_graph)
#         return scores

#     def result(self, text, lim):

#         sims = self.getSimMat(text)
#         scores = self.pageRank(sims)
#         limit = lim

#     # sorting upto the best valued sentences,,,,,,,,,,,,,
#         xx = dict(
#             sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit])

#         xy = sorted(xx.items(), key=lambda x: x[0])
#         # print(xy)
#         reslt = ''
#         for x in xy:
#             # print(sentences[x[0]])
#             reslt += '. ' + sentences[x[0]]

#         return reslt
