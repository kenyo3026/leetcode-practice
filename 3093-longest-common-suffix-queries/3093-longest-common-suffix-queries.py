class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        class Node:
            __slots__ = ('children', 'best_idx', 'best_len')
            def __init__(self):
                self.children = {}
                self.best_idx = -1
                self.best_len = float('inf')

        root = Node()

        def update(node, idx, length):
            if length < node.best_len:
                node.best_len = length
                node.best_idx = idx

        for i, w in enumerate(wordsContainer):
            node = root
            update(node, i, len(w))
            for c in reversed(w):
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                update(node, i, len(w))

        ans = []
        for q in wordsQuery:
            node = root
            for c in reversed(q):
                if c in node.children:
                    node = node.children[c]
                else:
                    break
            ans.append(node.best_idx)
        return ans