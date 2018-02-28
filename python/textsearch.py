"""
To run:

pip install hug
hug -f textsearch.py
"""
import collections
import glob
import os
import pickle
import string

import hug


Document = collections.namedtuple('Document', 'id title data')

docs_dir = 'docs'
index_file = 'index.pkl'


if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

if not os.path.exists(index_file):
    index = {}
    with open(index_file, 'wb') as fh:
        pickle.dump(index, fh)


def strip_symbols(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def create_document(id, title, data):
    title = strip_symbols(title)
    data = strip_symbols(data)
    doc = Document(id, title, data)
    file_name = os.path.join(docs_dir, doc.id)
    with open(file_name, 'w') as fh:
        content = '{}\n{}'.format(doc.title, doc.data)
        fh.write(content)


def parse_docs():
    doc_text, words = {}, set()
    for doc in glob.glob('{}/*'.format(docs_dir)):
        with open(doc, 'r') as f:
            text = f.read().split()
            words |= set(text)
            doc_name = doc.split('/')[-1]
            doc_text[doc_name] = text
    return doc_text, words


def update_index():
    doc_text, words = parse_docs()
    index = {}
    for word in words:
        index[word] = set(doc_name for doc_name, doc_text in doc_text.items()
                          if word in doc_text)
    with open(index_file, 'wb') as fh:
        pickle.dump(index, fh)


def word_search(word):
    with open(index_file, 'rb') as fh:
        index = pickle.load(fh)
    docs = index.get(word, [])
    return docs


def read_document(doc_id):
    content = open(os.path.join(docs_dir, doc_id)).read().splitlines()
    result = Document(doc_id, content[0], content[1])
    return result._asdict()


def phrase_search(phrase):
    pass


def words_search(query):
    results = collections.defaultdict(list)
    words = query.split()
    for word in words:
        docs = word_search(word)
        for doc in docs:
            results[doc].append(word)
    return results


def term_freq(word, doc_id):
    content = open(os.path.join(docs_dir, doc_id)).read().split()
    freq = content.count(word) / len(content)
    return freq


def tf(words, doc):
    freq = 0
    for word in words:
        freq += term_freq(word, doc)
    return freq


def sort_results(results):
    s_results = {}
    for doc, words in results.items():
        score = tf(words, doc)
        s_results[doc] = score
    docs = sorted(s_results, key=s_results.get, reverse=True)
    return docs


@hug.post()
def index(id, title, data):
    create_document(id, title, data)
    update_index()
    return 'Indexed submitted data'


@hug.get()
def search(request):
    query = request.params['q']

    if query.startswith('"') and query.endswith('"'):
        docs = phrase_search()
    else:
        results = words_search(query)
        docs = sort_results(results)
    return [read_document(doc) for doc in docs]


if __name__ == '__main__':
    index.interface.api()
    search.interface.api()
