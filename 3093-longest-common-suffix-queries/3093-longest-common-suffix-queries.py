class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self, depth=1):
                self.children = {}
                self.best_idx_so_far = -1
                self.best_len_so_far = float('inf')

        class Trie:
            def __init__(self, depth=1):
                self.root = TrieNode()

            def insert(self, word, idx):
                node = self.root
                if (lw:=len(word)) < node.best_len_so_far:
                    node.best_idx_so_far = idx
                    node.best_len_so_far = lw

                for char in reversed(word):
                    if not char in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    if (lw:=len(word)) < node.best_len_so_far:
                        node.best_idx_so_far = idx
                        node.best_len_so_far = lw

            def check(self, word):
                node = self.root
                for char in reversed(word):
                    if char in node.children:
                        node = node.children[char]
                    else:
                        break
                return node

        trie = Trie()

        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)

        matches = []
        for word in wordsQuery:
            matches.append(trie.check(word).best_idx_so_far)

        return matches