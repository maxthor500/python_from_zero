class WordFilter:

    def __init__(self, words: List[str]):
        self.dict = {}
        0
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.dict[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.dict.get((prefix, suffix), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)