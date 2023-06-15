class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        result = 0
        for coef, word in zip(coefs, words):
            result += coef * len(word)
        return result


    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words) or not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        result = 0
        for index, word in enumerate(words):
                result += coefs[index] * len(word)
        return result
