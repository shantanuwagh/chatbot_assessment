import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('wordnet')

with open('fruit.txt') as text:
    body_text = text.read()

def lemmatizer(text):
    return [nltk.WordNetLemmatizer().lemmatize(token.lower().strip(string.punctuation)) for token in nltk.word_tokenize(text) if token.lower().strip(string.punctuation)!='']

sentence_tokens = nltk.sent_tokenize(body_text)
tfidf_vector = TfidfVectorizer(tokenizer=lemmatizer, stop_words='english')

def response(input_text):
    sentence_tokens.append(input_text)
    tfidf_values = tfidf_vector.fit_transform(sentence_tokens)
    cosine_similarity_values = cosine_similarity(tfidf_values[-1], tfidf_values)
    best_sentence_id = cosine_similarity_values.argsort()[0][-2]
    best_sentence_tfidf = cosine_similarity_values[0][best_sentence_id]
    sentence_tokens.remove(input_text)
    if best_sentence_tfidf:
        return sentence_tokens[best_sentence_id]
    else:
        return None
