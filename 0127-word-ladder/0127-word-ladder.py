class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        n = len(beginWord)

        pattern_dict = {}
        for word in word_set:
            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]

                if pattern in pattern_dict:
                    pattern_dict[pattern].append(word)
                else:
                    pattern_dict[pattern] = [word]

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, step = queue.popleft()

            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]

                if not pattern in pattern_dict:
                    continue

                for similiar_word in pattern_dict[pattern]:

                    if similiar_word == endWord:
                        return step + 1

                    if similiar_word not in visited:
                        queue.append((similiar_word, step + 1))
                        visited.add(similiar_word)

        return 0