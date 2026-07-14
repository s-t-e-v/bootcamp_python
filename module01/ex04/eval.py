class Evaluator():
    @staticmethod
    def zip_evaluate(coefs: list[float], words: list[str]):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for coef, word in zip(coefs, words))

    @staticmethod
    def enumarate_evaluate(coefs: list[float], words: list[str]):
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(word) for i, word in enumerate(words))