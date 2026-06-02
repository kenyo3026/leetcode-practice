class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        class TrieNode:
            def __init__(self, depth=0):
                self.children = {}
                self.is_end = False
                self.suggestions = []

        class Trie:
            def __init__(self):
                self.root = TrieNode(0)

            def insert(self, word:str):
                node = self.root
                for char in word:

                    if not char in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]

                    if len(node.suggestions) < 3:
                        node.suggestions.append(word)

                node.is_end = True

            def suggest(self, word:str):
                node = self.root
                for char in word:
                    if not char in node.children:
                        return False
                    node = node.children[char]
                return node.suggestions

        trie = Trie()
        products = sorted(products)
        for product in products:
            trie.insert(product)

        node, suggestions = trie.root, []
        for char in searchWord:
            if node:
                node = node.children.get(char)
            suggestions.append(node.suggestions if node else [])
        return suggestions