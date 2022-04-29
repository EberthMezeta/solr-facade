from utils.tokenizer import tokenizer


class query_cleaner:

    def get_clean_query(self, query):

        tokenizer_object = tokenizer()
        tokens = []
        tokens = tokenizer_object.get_tokens(query)

        clean_query = ""
        for token in tokens:
            word = str(token)
            if word != 'not' and word != 'and' and word != 'or':
                clean_query = clean_query + word + '~ '
            else:
                clean_query = clean_query + word + ' '

        if len(tokens) == 0:
            clean_query = '*:*'
        return clean_query
