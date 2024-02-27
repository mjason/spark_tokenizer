import lib.iFlytekSpark_tokenization
import os


class Tokens(object):
    def __init__(self, tokenizer, text) -> None:
        self.encodes = tokenizer.encode(text)
        self.decodes = [tokenizer.decode(i) for i in self.encodes]
        self.size = len(self.encodes)


class Tokenizer(object):
    def __init__(self, vocab_file=(os.getenv("MODEL_PATH") or os.path.join(".", "models", "tokenizer"))) -> None:
        self.tokenizer = lib.iFlytekSpark_tokenization.iFlytekSparkSPTokenizer(
            vocab_file)

    def encode(self, text):
        return Tokens(self.tokenizer, text)
