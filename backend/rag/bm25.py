import math
import re

class BM25:
    def __init__(self, documents):
        self.docs = [self.tokenize(doc["text"]) for doc in documents]
        self.doc_lengths = [len(d) for d in self.docs]
        self.avgdl = sum(self.doc_lengths) / len(self.docs)
        self.k1 = 1.5
        self.b = 0.75

        # build vocabulary
        self.df = {}
        for doc in self.docs:
            for word in set(doc):
                self.df[word] = self.df.get(word, 0) + 1

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def score(self, query, index):
        score = 0.0
        tokens = self.tokenize(query)
        doc = self.docs[index]

        for word in tokens:
            if word not in doc:
                continue
            df = self.df.get(word, 0)
            idf = math.log((len(self.docs) - df + 0.5) / (df + 0.5) + 1)
            tf = doc.count(word)
            denom = tf + self.k1 * (1 - self.b + self.b * (self.doc_lengths[index] / self.avgdl))
            score += idf * ((tf * (self.k1 + 1)) / denom)

        return score

    def search(self, query):
        scores = []
        for i in range(len(self.docs)):
            score = self.score(query, i)
            scores.append((score, i))
        scores.sort(reverse=True)
        return scores
