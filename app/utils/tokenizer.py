import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords


class tokenizer:

    def get_tokens(self, query):
        # lower case
        clean_query = query.lower()
        # remove accents
        clean_query = unidecode.unidecode(clean_query)
        # tokenize
        tokens = word_tokenize(clean_query, language="spanish")
        # Remove punctuations, other formalities of grammar
        tokens = [word for word in tokens if word.isalpha()]
        # Remove white spaces and StopWords
        tokens = [
            word for word in tokens if not word in stopwords.words("spanish")]
        return tokens
