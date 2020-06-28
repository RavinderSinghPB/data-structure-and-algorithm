class Trie_node:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Trie_node()

    def getnode(self):
        return Trie_node()

    def _chartoindex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._chartoindex(key[i])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getnode()
            pCrawl.count += 1
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
        pCrawl.count += 1

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._chartoindex(key[i])
            if not pCrawl.children[index]:
                return 0
            pCrawl = pCrawl.children[index]
        if pCrawl != None:
            return pCrawl.count


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        t = Trie()
        for _ in range(n):
            # lString.append(input())
            t.insert(input())

        nqry = int(input())
        for _ in range(nqry):
            print(t.search(input()))
