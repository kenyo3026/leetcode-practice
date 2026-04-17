class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        genes = {'A', 'C', 'G', 'T'}
        bank = set(bank)

        n = len(startGene)
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            curr_gene, step = queue.popleft()

            if curr_gene == endGene:
                return step

            for i in range(n):
                for gene in genes:
                    next_gene = curr_gene[:i] + gene + curr_gene[i+1:]

                    if next_gene in bank and next_gene not in visited:
                        queue.append((next_gene, step+1))
                        visited.add(next_gene)

        return -1