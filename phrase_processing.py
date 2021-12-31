import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords


grammar = """
Chunk: {<.*>+}
        }<JJ>{"""


def extract_ne(phrase):
    words = word_tokenize(phrase)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, 'label') and t.label() == 'NE'
    )

def named_entities(phrase):
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    words = word_tokenize(phrase)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags)
    tree.draw()
