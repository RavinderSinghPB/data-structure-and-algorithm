# contributed by RavinderSinghPB
class TrieNode:

    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch) - ord('a')


def cti(ch):
    return ord(ch) - ord('a')


def insert(root, key):
    for e in key:
        idx = cti(e)

        if not root.children[idx]:
            root.children[idx] = TrieNode()

        root = root.children[idx]

    root.isEndOfWord = True

def countChildren(root):
    global index
    cnt=0

    for i in range(26):
        if root.children[i]:
            cnt+=1
            index=i
    return cnt


index=0

def walkTrie(root):
    global index
    index=0
    prfx=''

    while countChildren(root)==1 and not root.isEndOfWord:

        root=root.children[index]
        prfx+=chr(ord('a')+index)
    return prfx




def search(root, key):
    ans=''

    for e in key:
        idx = cti(e)

        if not root.children[idx] or root.isEndOfWord:
            return ans
        ans+=e

        root = root.children[idx]

    return ans


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = input().strip().split()
        strs=arr[0]

        t = Trie()

        for s in arr:
            insert(t.root, s)

        print(walkTrie(t.root))